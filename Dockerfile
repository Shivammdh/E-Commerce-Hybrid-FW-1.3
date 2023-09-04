FROM python:3.10-slim-buster as base

## start builder stage.

# this is the first stage of the build.
# it will install all requirements.
FROM base as builder

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget curl

# Download and install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Download and install ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}') && \
    CHROME_DRIVER_VERSION=$(curl -sS "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}") && \
    wget -q "https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip -d /usr/local/bin && \
    rm chromedriver_linux64.zip && \
    chmod +x /usr/local/bin/chromedriver

# copy any python requirements file into the install directory and install all python requirements.
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade --no-cache-dir -r requirements.txt
#RUN rm /requirements.txt # remove requirements file from container.

# copy the source code into /app and move into that directory.


COPY . .
## end builder stage.

#####

## start base stage.

# this is the image this is run.
FROM builder


CMD ["/bin/bash"]
# default entry point.
CMD ["python", "-m Tests.FlightBookingMain.py"]
## end base stage.
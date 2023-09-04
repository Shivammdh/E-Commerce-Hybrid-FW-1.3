from Utilites import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")

path="D:\Product-Compare-Muti-Sites\Results\E-Commerce-data.xlsx"
rows= XLUtils.getRowCout(path, 'Sheet1')
for r in range(2,rows+1):
        driver.maximize_window()
        driver.get("https://demo.guru99.com/test/newtours/")
        username= XLUtils.readData(path, 'Sheet1', r, 1)
        password= XLUtils.readData(path, 'Sheet1', r, 2)
        driver.find_element(By.XPATH,"//input[@name='userName']").send_keys(username)
        driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH,"//input[@name='submit']").click()

        if driver.title=="Login: Mercury Tours":
                print("Test Passed...")
                XLUtils.writeData(path, 'Sheet1', r, 3, 'Pass')

        else:
                print("Failed...")
                XLUtils.writeData(path, 'Sheet1', r, 3, 'Fail')

        # time.sleep(2)
        # driver.find_element(By.LINK_TEXT,"Home").click()
        # time.sleep(2)







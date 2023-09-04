import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Locators.amazon_locators import AmazonLocators as al
from Utilites.BasePage import BaseClass
from Utilites.matching_titles import is_similar_enough

class AmazonPage:
    '''Amazon locators and driver are initialized'''

    def __init__(self, driver):
        self.driver = driver
        self.awz_search_box=al.awz_search_box
        self.amz_product=al.amz_product
        self.amz_lang_btn = al.amz_lang_btn
        self.amz_lang_dropdwn = al.amz_lang_dropdwn
        self.amz_lang_save_btn = al.amz_lang_save_btn
        self.amz_price = al.amz_price
        self.amz_price2=al.amz_price2
        self.amz_rate = al.amz_rate
        self.amz_people_rate = al.amz_people_rate
        self.amz_rview = al.amz_rview


    def amazon_compare(self, source_link,product_name):
        driver = self.driver
        driver.get(source_link)
        # product_name=input("\nEnter Your Product Name: ")
        try:
            if driver.find_element(By.ID, "captchacharacters").is_displayed():
                captcha = input('Enter Captcha:')
                driver.find_element(By.ID, "captchacharacters").send_keys(captcha)
                time.sleep(2)
                driver.find_element(By.XPATH, "//button").click()
        except Exception:
            pass
        search_box = driver.find_element(By.ID,self.awz_search_box)
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            all_products=driver.find_elements(By.XPATH,self.amz_product)
            amz_product_lst=[]
            if len(all_products) > 0:
                print("*********************All Products Available In Amazon*********************")
                for product in all_products:
                    print("Product Name: ",product.text)
                    # print(f'Product Name {product[0]}     Price:{product[1]}')
                print("**************************************************************************")
            time.sleep(2)
            your_product = input("Enter your product name from above suggested list: ")
            for newprd in all_products:
                if newprd.text==your_product:
                    newprd.click()
                    break
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(10)
            base_obj = BaseClass(driver)
            time.sleep(3)
            try:
                if base_obj.verifywait(By.XPATH, self.amz_price).is_displayed():
                    a_price=base_obj.verifywait(By.XPATH, self.amz_price)

            except:
                a_price=base_obj.verifywait(By.XPATH,self.amz_price2)
            amazon_price = a_price.text
            amazon_rating = driver.find_element(By.XPATH, self.amz_rate).text
            amazon_pepol_rate = driver.find_element(By.ID, self.amz_people_rate).text
            amazon_review = driver.find_element(By.XPATH, self.amz_rview).text
            time.sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            return amazon_price, amazon_rating, amazon_pepol_rate, amazon_review
        except:
            return None,None,None,None

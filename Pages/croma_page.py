import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Locators.croma_locators import CromaLocators as cl
from Utilites.BasePage import BaseClass
from selenium.webdriver.support import expected_conditions as EC

from Utilites.matching_titles import is_similar_enough


class CromaPage:
    '''flipkart locators and driver are initialized'''

    def __init__(self, driver):
        self.driver = driver
        self.croma_search_box=cl.croma_search_box
        self.croma_product=cl.croma_product
        self.custom_icon=cl.custom_icon
        self.croma_custom_icon = cl.croma_custom_icon
        self.croma_price = cl.croma_price
        self.croma_rate = cl.croma_rate
        self.croma_rating_review = cl.croma_rating_review

    def croma_compare(self,source_link,product_name):
        driver = self.driver
        flwait = WebDriverWait(driver, timeout=30, poll_frequency=5, ignored_exceptions=[NoSuchElementException])

        # driver.switch_to.new_window('WINDOW')
        driver.get(source_link)
        # product_name=input("\nEnter your Product Name: ")
        try:
            if flwait.until(EC.presence_of_element_located((By.ID, self.croma_search_box))).is_displayed():
                pass
        except:
            driver.refresh()
        search_box = driver.find_element(By.ID, self.croma_search_box)
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        try:
            croma_products = driver.find_elements(By.XPATH, self.croma_product)
            if len(croma_products)>0:
                print("*********************All Products Available In Amazon*********************")
                for product in croma_products:
                    print("Product Name: ", product.text)
                    # print(f'Product Name {product[0]}     Price:{product[1]}')
                print("**************************************************************************")

                time.sleep(2)
                your_product = input("Enter your product name from above suggested list: ")
                for newprd in croma_products:
                    if newprd.text == your_product:
                        newprd.find_element(By.XPATH,"a").click()
                        break
                time.sleep(3)
                # product.click()
                driver.switch_to.window(driver.window_handles[1])
                driver.implicitly_wait(10)
                try:
                    if flwait.until(EC.presence_of_element_located((By.ID, self.custom_icon))).is_displayed():
                        driver.find_element(By.ID, self.custom_icon).click()
                except:
                    pass
                time.sleep(2)
                driver.implicitly_wait(10)
                wait = BaseClass(driver)
                try:
                    if wait.verifywait(By.ID, self.croma_price).is_displayed():
                        pass
                except:
                    driver.refresh()

                try:
                    if wait.verifywait(By.ID, self.croma_custom_icon).is_displayed():
                        driver.find_element(By.ID, self.croma_custom_icon).click()
                except:
                    pass
                time.sleep(1)
                c_price = driver.find_element(By.ID, self.croma_price)
                corma_price = c_price.text
                corma_rating = driver.find_element(By.XPATH, self.croma_rate).text
                corma_rating_reviws = driver.find_element(By.XPATH, self.croma_rating_review).text
                corma_r_v = corma_rating_reviws.split('&')
                corma_pepole_rating = corma_r_v[0]
                corma_pepole_review = corma_r_v[1]
                return corma_price, corma_rating, corma_pepole_rating, corma_pepole_review
        except:
            return None,None,None,None

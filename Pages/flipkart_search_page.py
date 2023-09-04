import time
from pprint import pprint

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from Locators.flipkart_locators import FlipkartSearchLocators as fsl
from Utilites.modify_data import ModifyData
from Pages.flipkart_item_selection_page import FlipkartItem

class FlipkartSearch:
    def __init__(self,driver):
        self.driver=driver
        self.pop_up=fsl.pop_up
        self.search_box=fsl.search_box
        self.product_title=fsl.product_title
        self.product_title2=fsl.product_title2
        self.b_product_title=fsl.b_product_title
        self.b_price=fsl.b_price
        self.price2=fsl.price2
        self.b_link=fsl.b_link
        self.f_price=fsl.f_price
        self.f_link=fsl.f_link

    def flipkart_search(self,flipkart_link,product_name):
        priceobj = ModifyData()
        driver=self.driver
        fk_items_dtl_obj = FlipkartItem(driver)
        list_items = []
        driver.get(flipkart_link)
        try:
            close_popup = driver.find_element(By.XPATH,self.pop_up)
            close_popup.click()
        except NoSuchElementException:
            pass

        search_box = driver.find_element(By.NAME,self.search_box)
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        try:
            product_titles = driver.find_elements(By.XPATH, self.product_title)
            if len(product_titles)>0:
                list_items=fk_items_dtl_obj.item_detail(product_titles,product_name)
                print("*********************All Products Available In Flipkart*********************")
                for product in list_items:
                    print(f'Product Name {product[0]}     Price:{product[1]}')
                print("*************************************************************************")

                your_product = input("Enter your product name name from above suggested list: ")
                for product in list_items:
                    if your_product == product[0]:
                        all_details=fk_items_dtl_obj.item_selection(product[0],product_titles)
                        # print(all_details)
                        return all_details
            else:
                item_details = driver.find_elements(By.XPATH, "//div[@class='_13oc-S']/div/div")
                for p in item_details:
                    product_title = p.find_element(By.XPATH, "div/a[1]").text
                    price = p.find_element(By.XPATH, "div/a[2]/div/div[1][contains(text(),'₹')]").text
                    # print(price)
                    mdprice = priceobj.modify_price(price)
                    link = p.find_element(By.XPATH, "a").get_attribute('href')
                    list_items.append([product_title, mdprice, link])
                # print(list_items)
                lowest_price_product = min(list_items, key=lambda x: x[1])
                return lowest_price_product
        except Exception as ec:
            return None,None,None,None,None
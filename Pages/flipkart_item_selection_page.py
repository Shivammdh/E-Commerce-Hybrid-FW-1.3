import time

from selenium.webdriver.common.by import By

from Locators.flipkart_locators import FlipkartSearchLocators as fsl
from Pages.flipkart_page import FlipkartPage
from Utilites.modify_data import ModifyData


class FlipkartItem:
    def __init__(self, driver):
        self.driver = driver
        self.pop_up = fsl.pop_up
        self.search_box = fsl.search_box
        self.product_title = fsl.product_title
        self.product_title2 = fsl.product_title2
        self.b_product_title = fsl.b_product_title
        self.b_price = fsl.b_price
        self.price2 = fsl.price2
        self.b_link = fsl.b_link
        self.f_price = fsl.f_price
        self.f_link = fsl.f_link

    def item_detail(self, product_titles, product_name):
        driver = self.driver
        list_items = []
        priceobj = ModifyData()
        for p in product_titles:
            if p.text == 'Sponsored':
                pass
            elif p.text == '':
                title = driver.find_element(By.XPATH, self.b_product_title).text
                price = driver.find_element(By.XPATH, self.b_price).text
                link = driver.find_element(By.XPATH, self.b_link).get_attribute('href')
                list_items.append([title,price, link])
            else:
                title = p.text
                price = p.find_element(By.XPATH, self.f_price).text
                link = driver.find_element(By.XPATH, self.f_link).get_attribute('href')
                list_items.append([title,price,link])

        return list_items


    def item_selection(self, product_name, product_titles):
        driver = self.driver
        priceobj = ModifyData()
        fp_obj = FlipkartPage(driver)

        for p in product_titles:
            if p.text == 'Sponsored':
                pass
            elif p.text == '':
                title = driver.find_element(By.XPATH, self.b_product_title).text
                if product_name.lower() in title.lower():
                    p.click()
                    time.sleep(3)
                    driver.switch_to.window(driver.window_handles[1])
                    result = fp_obj.flipkart_compare()
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    return result
                    # break
            else:
                title = p.text
                if product_name.lower() in title.lower():
                    p.click()
                    time.sleep(5)
                    driver.switch_to.window(driver.window_handles[1])
                    result = fp_obj.flipkart_compare()
                    time.sleep(3)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    # print(result)
                    return result


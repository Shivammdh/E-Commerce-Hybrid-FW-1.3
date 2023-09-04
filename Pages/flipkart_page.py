from selenium.webdriver.common.by import By

from Locators.flipkart_locators import FlipkartLocators as fl
from Utilites.avrage import find_avrage

class FlipkartPage:
    '''flipkart locators and driver are initialized'''

    def __init__(self, driver):
        self.driver = driver
        self.fk_price1 = fl.fk_price1
        self.fk_price2 = fl.fk_price2
        self.fk_price3 = fl.fk_price3
        self.product_name1 = fl.product_name1
        self.product_name2 = fl.product_name2
        self.fk_rate = fl.fk_rate
        self.fk_tot_rating = fl.fk_tot_rating
        self.fk_review = fl.fk_review

    def flipkart_compare(self):
        driver = self.driver
        # driver.get(source1)
        driver.implicitly_wait(10)
        try:
            if driver.find_element(By.XPATH, self.fk_price1).is_displayed():
                f_price = driver.find_element(By.XPATH, self.fk_price1)
            elif driver.find_element(By.XPATH, self.fk_price3).is_displayed():
                f_price = driver.find_element(By.XPATH, self.fk_price3)
        except Exception:
            f_price = driver.find_element(By.XPATH, self.fk_price2)
        try:
            if driver.find_element(By.XPATH, self.product_name1).is_displayed():
                pr_name = driver.find_element(By.XPATH, self.product_name1)
        except:
            pr_name = driver.find_element(By.XPATH, self.product_name2)
        product = pr_name.text
        flipkart_price = f_price.text
        flipkart_rating = driver.find_element(By.CSS_SELECTOR, self.fk_rate).text
        flipkart_people_rate = driver.find_element(By.XPATH, self.fk_tot_rating).text
        flipkart_review = driver.find_element(By.XPATH, self.fk_review).text
        five_star = driver.find_element(By.XPATH, "//ul[@class='_36LmXx']/li[1]").text
        one_star = driver.find_element(By.XPATH, "//ul[@class='_36LmXx']/li[5]").text
        average_five_star, average_one_star=find_avrage(five_star,one_star)
        return product, flipkart_price, flipkart_rating, flipkart_people_rate, flipkart_review,average_five_star,average_one_star

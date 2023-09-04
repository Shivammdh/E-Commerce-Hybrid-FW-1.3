import os
import sys
import time
from selenium import webdriver
from Pages.amazone_page import AmazonPage
from Pages.croma_page import CromaPage
from Pages.display_page import Display
from Pages.flipkart_page import FlipkartPage
from Utilites.comparision import compare_products
from Utilites.modify_data import ModifyData
import unittest
from Utilites.PassArgument import browser,excu
from Utilites.failuer import TestFail
from Utilites.hub_node_conection import start_grid,close_grid
from Configure.configfilereader import get_data
import logging
from Pages.flipkart_search_page import FlipkartSearch
from Utilites import write_test_result

logging.basicConfig(filename=r"D:\Product-Compare-Muti-Sites\logReport\test.log", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',filemode='w')

# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
class EcommerceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.flipkart_link,cls.amazon_link,cls.croma_link,cls.remote_link=get_data()
        cls.test = TestFail()
        # cls.croma_link="https://www.croma.com/"
        cls.hbflag=False
        cls.excu = excu
        cls.browser = browser
        cls.product_name = input("\nEnter product name: ")
        # create a webdriver object for chrome-option and configure
        option = webdriver.ChromeOptions()
        option.page_load_strategy = 'normal'
        # option.binary_location=".//"
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument('--ignore-certificate-errors')
        option.add_argument('--start-maximized')
        option.add_experimental_option("useAutomationExtension", False)
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--disable-blink-features=AutomationControlled")
        cls.flag = False
        if excu == 'Local':
            # logging.info(f"Starting Program in {excu}, Please wait ...")
            if browser == 'chrome':
                cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
                cls.driver.implicitly_wait(30)
            elif browser == 'firefox':
                cls.driver = webdriver.Firefox(options=option)
                cls.driver.implicitly_wait(30)
            elif browser == 'MicrosoftEdge':
                cls.driver = webdriver.Edge(options=option)
                cls.driver.implicitly_wait(30)

            else:
                print("Please choose correct browser")
        if excu == 'Grid':
            # logging.info(f"Starting Program in {excu}, Please wait ...")
            '''
            Connecting hub and node automatically By using start_grid() function from
            Utilites.hub_node_conection module
            '''
            cls.hub,cls.node=start_grid()
            time.sleep(40)
            cls.hbflag=True
            print('Hub and Node connected Successfully....')
            if browser == "chrome":
                print(f"Running the test script on {browser} browser")
                cls.driver = webdriver.Remote(command_executor=cls.remote_link,
                                          options=option)

            elif browser == "firefox":
                print(f"Running the test script on {browser} browser")
                cls.driver= webdriver.Remote(command_executor=cls.remote_link,
                                          options=option)
            elif browser=='MicrosoftEdge':
                print(f"Running the test script on {browser} browser")
                cls.driver = webdriver.Remote(command_executor=cls.remote_link,
                                              options=option)
            else:
                print('Choose correct Browser..')

        """
        if excu == 'saucelab':
            if browser == 'chrome':
                options = webdriver.ChromeOptions()
                options.browser_version = 'latest'
                options.platform_name = 'Windows 10'

                sauce_url = "https://oauth-shivamsharmamdh-6984d:5750d6be-5e92-431c-9f65-01c0683b16e0@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
                cls.driver = webdriver.Remote(command_executor=sauce_url, options=options)

                cls.driver.get("https://app.keka.com/Account/KekaLogin?returnUrl=%2F")
                cls.action = ActionChains(cls.driver)
                cls.wait = WebDriverWait(cls.driver, 60)
            elif browser == 'firefox':
                options = webdriver.FirefoxOptions()
                options.browser_version = 'latest'
                options.platform_name = 'Windows 10'

                sauce_url = "https://oauth-shivamsharmamdh-6984d:5750d6be-5e92-431c-9f65-01c0683b16e0@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
                cls.driver = webdriver.Remote(command_executor=sauce_url, options=options)
                cls.wait = WebDriverWait(cls.driver, 60)

            else:
                print("Please choose correct driver")
                """
        print("*************************************************************************** \n")
        print("                     Starting Program, Please wait ..... \n")
        logger.info(f"Starting Program in {browser} and {excu}, Please wait ...")
        print("*************************************************************************** \n")
    @classmethod
    def test_flipkart_page(cls):
        try:
            print("Connecting to Flipkart")
            fp_search=FlipkartSearch(cls.driver)
            # cls.item_details=fp_search.flipkart_search(cls.flipkart_link,product_name)
            f_test=True
            logger.info("Connecting to Flipkart")
            # flipkart_obj = FlipkartPage(cls.driver)
            cls.product, cls.flipkart_price, cls.flipkart_rating, cls.flipkart_people_rate, cls.flipkart_review,cls.avg_five_star,cls.avg_one_star = fp_search.flipkart_search(cls.flipkart_link,cls.product_name)
            print(" ---> Successfully retrieved the data from Flipkart \n")
            time.sleep(2)
            logger.info("Test flipkart page pass...")
            print("*************************************************************************** \n")
        except Exception as e:
            f_test = False
            cls.driver.save_screenshot('D:\\Product-Compare-Muti-Sites\\ScreenShots\\flipkart_page.png')
            cls.test.test_fail(f"Test case 1 failed with exception: {e}")
            logger.exception("Test case 1 failed with exception: %s", e)

        write_test_result.write_result(f_test, 2)

    @classmethod
    def test_amazon_page(cls):
        try:
            a_test=True
            print("Connecting to Amazon")
            logger.info("Connecting to Amazon")
            print("*************************************************************************** \n")
            amazon_obj = AmazonPage(cls.driver)
            # amz_product_name=input("Enter Product Name: ")
            cls.amazon_price, cls.amazon_rating, cls.amazon_pepol_rate, cls.amazon_review = amazon_obj.amazon_compare(cls.amazon_link,cls.product_name)
            print(" ---> Successfully retrieved the data from Amazon \n")
            time.sleep(2)
            logger.info("Test Amazon page pass...")
            print("*************************************************************************** \n")
        except Exception as e:
            a_test = False
            cls.driver.save_screenshot('D:\\Product-Compare-Muti-Sites\\ScreenShots\\Amazon_page.png')
            cls.test.test_fail(f"Test case 2 failed with exception: {e}")
            logger.exception("Test case 2 failed with exception: %s", e)

        write_test_result.write_result(a_test, 3)

    @classmethod
    def test_croma_page(cls):
        try:
            c_test=True
            print("Connecting to Croma")
            logger.info("Connecting to Croma")
            print("*************************************************************************** \n")
            croma_obj = CromaPage(cls.driver)
            cls.corma_price, cls.corma_rating, cls.corma_pepole_rating, cls.corma_pepole_review = croma_obj.croma_compare(cls.croma_link,cls.product_name)
            print(" ---> Successfully retrieved the data from Croma\n")
            time.sleep(2)
            print("*************************************************************************** \n")
            logger.info("Test croma page pass...")
        except Exception as e:
            c_test = False
            cls.driver.save_screenshot('D:\\Product-Compare-Muti-Sites\\ScreenShots\\croma_page.png')
            cls.test.test_fail(f"Test case 3 failed with exception: {e}")
            logger.exception("Test case 3 failed with exception: %s", e)

        write_test_result.write_result(c_test, 4)


    @classmethod
    def test_display_info(cls):
        # Final display
        try:
            disp_test=True
            cls.display_obj = Display()
            logger.info('Display page')
            print("#------------------------------------------------------------------------#")
            cls.display_obj.display_flipkart_data(cls.product, cls.flipkart_price, cls.flipkart_rating,cls.flipkart_people_rate, cls.flipkart_review)
            print("#------------------------------------------------------------------------#")
            cls.display_obj.display_amazon_data(cls.amazon_price, cls.amazon_rating, cls.amazon_pepol_rate,cls.amazon_review)
            print("#------------------------------------------------------------------------#")
            cls.display_obj.display_croma_data(cls.corma_price, cls.corma_rating, cls.corma_pepole_rating,cls.corma_pepole_review)
            logger.info("Test display page pass...")
            print("*************************************************************************** \n")
        except Exception as e:
            disp_test = False
            cls.test.test_fail(f"Test case 4 failed with exception: {e}")
            logger.exception("Test case 4 failed with exception: %s", e)

        write_test_result.write_result(disp_test, 5)

    @classmethod
    def test_modify_data_values(cls):
        try:
            mod_test=True
            logger.info('Data Modifying')
            # Modify Data Values
            # Create object for ModifyData class
            cls.modify_obj=ModifyData()
            # Call the method modify_price_data() from ModifyData class for modifying price data
            cls.prices=cls.modify_obj.modify_price_data(cls.flipkart_price, cls.amazon_price, cls.corma_price)

            # Call the method modify_people_rate_data() from ModifyData class for modifying people rate data
            cls.total_peoples_rating = cls.modify_obj.modify_people_rate_data(cls.flipkart_people_rate, cls.amazon_pepol_rate, cls.corma_pepole_rating)

            # # Call the method modify_reviews() from ModifyData class for modifying people reviews data
            cls.reviews=cls.modify_obj.modify_reviews(cls.flipkart_review, cls.amazon_review, cls.corma_pepole_review)

            # Call the method modify_people_rate_data() from ModifyData class for modifying people rate data
            cls.ratings=cls.modify_obj.modify_rating_in_stars(cls.flipkart_rating, cls.amazon_rating, cls.corma_rating)
            print('Data Modified successfully...')
            logger.info("Test modify data pass...")
            print("*************************************************************************** \n")
        except Exception as e:
            mod_test = False
            cls.test.test_fail(f"Test case 5 failed with exception: {e}")
            logger.exception("Test case 5 failed with exception: %s", e)

        write_test_result.write_result(mod_test, 6)

    @classmethod
    def test_compare_product_and_display(cls):
        try:
            cpr_test=True
            logger.info("Display Information's")
            company = ['FlipKart', 'Amazon', 'Corma']
            lowest_price_product, highest_rating_product, highest_num_ratings_product,highest_reviews = compare_products(cls.prices, cls.ratings, cls.total_peoples_rating,cls.reviews)
            # print("########################################################################")
            # print(lowest_price_product)
            # print(highest_rating_product)
            # print(highest_num_ratings_product)
            # print(highest_reviews)
            # print("########################################################################")
            products_info = list(zip(company, cls.prices, cls.ratings, cls.total_peoples_rating, cls.reviews))
            # print("########################################################################")
            # pprint(products_info)
            # print("########################################################################")

            dct = {}
            for tup in products_info:
                dct[tup[0]] = tup[1:]
            # Output the result
            # print("########################################################################")
            # pprint(dct)
            # print("########################################################################")
            print(f"\n{cls.product} with Lowest Price:")
            for k, v in dct.items():
                if lowest_price_product[0] in v:
                    print(
                        f"Company:{k},Price: {lowest_price_product[0]}, Rating: {lowest_price_product[1]}, Number of Ratings: {lowest_price_product[2]}, Number of reviews: {lowest_price_product[3]}")
                    write_test_result.write_product_result(k,lowest_price_product[0],2)
                    break

            print(f"\n{cls.product} with Highest Rating:")
            for k, v in dct.items():
                if highest_rating_product[1] in v:
                    print(
                        f"company:{k},Price: {highest_rating_product[0]}, Rating: {highest_rating_product[1]}, Number of Ratings: {highest_rating_product[2]}, Number of reviews: {highest_rating_product[3]}")
                    write_test_result.write_product_result(k, highest_rating_product[1], 3)
                    break
            print(f"\n{cls.product} with Highest Number of Ratings:")
            for k, v in dct.items():
                if highest_num_ratings_product[2] in v:
                    print(
                        f"Company:{k},Price: {highest_num_ratings_product[0]}, Rating: {highest_num_ratings_product[1]}, Number of Ratings: {highest_num_ratings_product[2]},Number of reviews: {highest_num_ratings_product[3]}")
                    write_test_result.write_product_result(k, highest_num_ratings_product[2], 4)
                    break
            print(f"\n{cls.product} with Highest Number of Reviews:")
            for k, v in dct.items():
                if highest_reviews[3] in v:
                    print(
                        f"Company:{k},Price: {highest_reviews[0]}, Rating: {highest_reviews[1]}, Number of Ratings: {highest_reviews[2]},Number of reviews: {highest_reviews[3]}")
                    write_test_result.write_product_result(k, highest_reviews[3], 5)
                    break
            logger.info("Test compare page pass...")
        except Exception as e:
            cpr_test=False
            cls.test.test_fail(f"Test case 6 failed with exception: {e}")
            logger.exception(f"Test case 6 failed with exception: {e}")
        write_test_result.write_result(cpr_test,7)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logger.info('Closing the browser...')
        if cls.hbflag:
            close_grid(cls.hub,cls.node)
            logger.info('Hub And Node Terminated successfully...')



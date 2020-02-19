from selenium import webdriver
from time import sleep
import os


class WholeFoodsBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://amazon.com')

        sleep(1)
        sign_in_btn = self.driver.find_element_by_xpath(
            '//*[@id="nav-signin-tooltip"]/a')
        sign_in_btn.click()

        sleep(1)
        username_field = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]')
        username_field.send_keys(os.environ['AMAZON_USERNAME'])
        continue_btn = self.driver.find_element_by_xpath('//*[@id="continue"]')
        continue_btn.click()

        password_field = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input')
        password_field.send_keys(os.environ["AMAZON_PASSWORD"])
        submit_btn = self.driver.find_element_by_xpath(
            '//*[@id="signInSubmit"]')
        submit_btn.click()

        whole_foods_button = self.driver.find_element_by_xpath(
            '//*[@id="nav-xshop"]/a[2]')
        whole_foods_button.click()

        sleep(1)
        whole_foods_search = self.driver.find_element_by_xpath(
            '//*[@id="twotabsearchtextbox"]')
        whole_foods_search.send_keys('shelled edamame')

        edamame_add = self.driver.find_element_by_xpath(
            '//*[@id="B074H61RXS-add-to-cart"]/span/input')

        for _ in range(14):
            edamame_add.click()

    def close(self):
        self.driver.close()


bot = WholeFoodsBot()
bot.login()
# bot.close()

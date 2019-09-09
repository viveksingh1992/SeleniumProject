from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import HtmlTestRunner

from POM.Page.loginPage import LoginPage


class LoginTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://dev.castinet.org/")

    def test_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("ptyagi@dminc.com")
        login.click_usernameNext()
        login.enter_password("Jupiter@20")
        time.sleep(5)
        login.click_passwordNext()
        login.click_signIn()
        message = driver.title
        self.assertEqual(message, "Home | CASTiNET")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vivsingh/PycharmProjects/SeleniumProject'
                                                                  '/reports'))

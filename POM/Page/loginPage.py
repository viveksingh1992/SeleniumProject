from POM.Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_xpath = Locators.username_textbox_xpath
        self.username_nextButton_xpath = Locators.username_nextButton_xpath
        self.password_textbox_xpath = Locators.password_textbox_xpath
        self.password_nextButton_xpath = Locators.password_nextButton_xpath
        self.signIn_Button_xpath = Locators.signIn_Button_xpath

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def click_usernameNext(self):
        self.driver.find_element_by_xpath(self.username_nextButton_xpath).click()

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_passwordNext(self):
        self.driver.find_element_by_xpath(self.password_nextButton_xpath).click()

    def click_signIn(self):
        self.driver.find_element_by_xpath(self.signIn_Button_xpath).click()

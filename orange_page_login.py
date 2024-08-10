from selenium.webdriver.common.by import By

class OrangeLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_locator = (By.XPATH, '//input[@placeholder="Username"]')
        self.password_locator = (By.XPATH, '//input[@placeholder="Password"]')
        self.login_button_locator = (By.XPATH, '//button[@type="submit"]')

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_locator).click()
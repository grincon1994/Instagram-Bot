from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = "the account you want to target"
username = "your username"
pw = "your password"

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        username_placeholder = self.driver.find_element(By.XPATH,'//*[contains(@name, "username")]')
        username_placeholder.send_keys(username)
        time.sleep(4)
        password_placeholder = self.driver.find_element(By.XPATH,'//*[contains(@name, "password")]')
        password_placeholder.send_keys(pw)
        time.sleep(4)
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
        login_btn.click()
        

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(1)
        random_popup = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/svg/line'
        time.sleep(5)
        try:
            closing_popup = self.driver.find_element(By.XPATH, random_popup)
            if (closing_popup):
                closing_popup.click()
        except:
            print("popup not shown")     
        select_followers = self.driver.find_element(By.XPATH, '//*[contains(text(), "followers")]')
        select_followers.click()
        time.sleep(5)
        scroll_div = self.driver.find_element(By.XPATH, '//*[contains(@class, "x1ccrb07")]')
        for i in range (5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_div)
            time.sleep(2)
        

    def follow(self):
        dialog = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        follow_elements = dialog.find_elements(By.TAG_NAME, value='button')
        for button in follow_elements:
            try:
                button.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.XPATH, value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
                cancel_btn.click()

bot = InstaFollower()   
bot.login()
time.sleep(10)
bot.find_followers()
bot.follow()
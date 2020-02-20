from selenium import webdriver
from time import sleep
from getpass import getpass

TINDER = 'https://tinder.com'

#region Title
TITLE = """
 ________  __                  __                            _______              __     
|        \|  \                |  \                          |       \            |  \    
 \$$$$$$$$ \$$ _______    ____| $$  ______    ______        | $$$$$$$\  ______  _| $$_   
   | $$   |  \|       \  /      $$ /      \  /      \       | $$__/ $$ /      \|   $$ \  
   | $$   | $$| $$$$$$$\|  $$$$$$$|  $$$$$$\|  $$$$$$\      | $$    $$|  $$$$$$\\$$$$$$  
   | $$   | $$| $$  | $$| $$  | $$| $$    $$| $$   \$$      | $$$$$$$\| $$  | $$ | $$ __ 
   | $$   | $$| $$  | $$| $$__| $$| $$$$$$$$| $$            | $$__/ $$| $$__/ $$ | $$|  
   | $$   | $$| $$  | $$ \$$    $$ \$$     \| $$            | $$    $$ \$$    $$  \$$  $$
    \$$    \$$ \$$   \$$  \$$$$$$$  \$$$$$$$ \$$             \$$$$$$$   \$$$$$$    \$$$$ 
                                                                                                                                                                                
"""
#endregion

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    

class TinderBot:

    def __init__(self):
        self.web = webdriver.Chrome()

    
    def login(self, username, password):
        self.web.get(TINDER)

        #login_btn = self.web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        #login_btn.click()

        sleep(3)
        login_with_facebook = self.web.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        login_with_facebook.click()

        #new facebook login window
        tinder_window, facebook_window = self.web.window_handles
        self.web.switch_to_window(facebook_window)

        #facebook login
        facebook_username_textbox = self.web.find_element_by_xpath('//*[@id="email"]')
        facebook_password_textbox = self.web.find_element_by_xpath('//*[@id="pass"]')
        facebook_login_button = self.web.find_element_by_xpath('//*[@id="u_0_0"]')

        facebook_username_textbox.send_keys('username')
        facebook_password_textbox.send_keys('password')
        facebook_login_button.click()

        self.web.switch_to_window(tinder_window)

    def swipe_right(self,numTimes: int) -> None:
        like_button = self.web.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]/span/svg/path')

        i = 0
        try:
            while i < numTimes:
                like_button.click()
                sleep(2)
                i += 1
        except:
            print("Out of likes for today. exiting.")
            exit(1)




def run():
    print(TITLE)

    print("Please enter the Facebook email used to login to Tinder: ")
    username = input("Email: ")
    password = getpass("Enter your password: ")
    confirm_password = getpass("Confirm Password: ")
    if(password != confirm_password):
        print("Passwords do not match. Exiting.")
        exit(1)
    print("Starting Bot...")
    tinder = TinderBot()
    tinder.login()
    tinder.swipe_right(10)


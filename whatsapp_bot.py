 
# ----------------------------------------------------------------------
# author : keshan
# program descripton : whatsapp bot that auto replies to msgs
# date : 03:11PM on June 27, 2019
# ----------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import threading
# from bs4 import BeautifulSoup as bs


class Whatsapp:
    # init method
    def __init__(self):
        chromepath = r'C:\webdrivers\chromedriver'
        self.driver = webdriver.Chrome(executable_path=chromepath)
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(25)
        self.target = 'Shehan'
        elem = None
        
        while elem is None:
            try:
                elem = self.driver.find_element_by_xpath('//span[@title="' + self.target + '"]')
            except:
                self.logout()

        ac = ActionChains(self.driver)
        ac.move_to_element(elem).click().perform()
        time.sleep(2)
        self.layer = self.driver.find_element_by_xpath('//div[@class="_1ays2"]')

    # method to logout of the web session if needed call function
    def logout(self):
        ham = self.driver.find_element_by_xpath(
            '//div[@title="Menu"]')
        ham.click()
        time.sleep(4)
        ham.find_element_by_xpath(
            '//div[@class="_2hHc6 T6CTG"]/ul[@class="_3z3lc"]/li[@class="_3cfBY _2yhpw _3BqnP"]/div[@title="Log out"]').click()

    # method that returns the last msg sent by the recipient
    def get_msg(self):
        no_div = False
        # scrolls to the height of the page
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        try:
            # gets the list of msgs recieved
            msgs = [msg.text for msg in self.layer.find_elements_by_xpath(
                "//div[@class='_1zGQT _2ugFP message-in tail']//span[@class='selectable-text invisible-space copyable-text']")]
            print(msgs)
            # returns the last index of the list result
            return msgs[-1].lower()
        except Exception:
            no_div = True
        
        if no_div:
            try:
                # gets the list of msgs recieved
                msgs = [msg.text for msg in self.layer.find_elements_by_xpath(
                    "//div[@class='_1zGQT _2ugFP message-in']//span[@class='selectable-text invisible-space copyable-text']")]
                print(msgs)
                # returns the last index of the list result
                return msgs[-1]
            except Exception as e:
                print(e)
        else:
            pass
       
    # method that gets the msgs and replied to them as programmed
    def chat(self):
        IsNew = False
        # run the class continuosly for each 15 seconds
        threading.Timer(10, self.chat).start()
        try:
            last_msg = self.get_msg()
            print(f"last msg by {self.target}:  "+last_msg)
            # gets all the divs that contains the msgs (in and out)
            last_reply = [msg.get_attribute('data-pre-plain-text') for msg in self.layer.find_elements_by_xpath("//div[@class='-N6Gq']//div[@class='copyable-text']")]
            # gets the last div of the above result and splits it to get the target name
            person = last_reply[-1].split(' ')
            # temporary variable
            tmp = self.target+':'
            # checks if the target name matches the result
            if person[2] == tmp:
                # if the target matches, then set the new var as true so the program can identify the msg and reply to it
                # this is used here because to avoid repitive messages being sent 
                # if the program had replied once then it waits for the next msg to reply
                IsNew = True

            # if the last msg was sent or recieved
            # will run only if the last msg is recieved
            if IsNew:
                if last_msg == 'hello':
                    reply = f'hey {self.target}'
                elif last_msg == 'whats up':
                    reply = "Nothing much. What about you?"
                elif last_msg == 'bye':
                    reply = f'okay bye {self.target}'
                elif last_msg == 'whats ur name':
                    reply = "I'm keshan's bot. Nice to meet you!"
                elif last_msg == 'i love you':
                    reply = "Aww. I love you too"
                else:
                    reply = '''sorry, i didnt get that. I'm still learning.
                    keshan didnt teach me well.            
                    '''
                
                # find the text box
                input_box = self.driver.find_element_by_xpath(
                '//div[@class="_3u328 copyable-text selectable-text"]')
                # focus on it by clicking
                input_box.click()
                # send the msg value as the reply
                input_box.send_keys(reply)
                # find the send button and click it
                self.driver.find_element_by_xpath('//span[@data-icon="send"]').click()
                # once the msg is sent . clear the text box
                # to avoid old msgs being sent 
                input_box.clear()
            else:
                print("\nYou replied last")

        except Exception as e:
            print(f"Error : {e}")


# create instance of class
if __name__ == '__main__':
    bot = Whatsapp()
    bot.chat()

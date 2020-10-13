from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

class speedtest_bot():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox"); 
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)

    def check_internet_speed(self):
        driver = self.driver
        driver.get("https://www.speedtest.net/")
        try:
            consent_button = driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
            consent_button.click()
        except:
            pass
        speedtest_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]')
        speedtest_button.click()
        time.sleep(130)
        ping_result = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]').text
        downloadingspeed_result = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]').text
        uploadingspeed_result = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]').text

        current_time = datetime.datetime.today()
        date = str(current_time)[:-7].strip()

        print("["+str(date) +"] Ping: "+ str(ping_result) +" | Download: "+ str(downloadingspeed_result) +" Mbps | Upload: "+str(uploadingspeed_result) +" Mbps")

        ping_result_int = int(ping_result)
        if ping_result_int > 4:
            print("Warning high ping value")
        downloadingspeed_result_float = float(downloadingspeed_result)
        if downloadingspeed_result_float < 10:
            print("Warning low downloading speed")
        uploadingspeed_result_float = float(uploadingspeed_result)
        if uploadingspeed_result_float < 10:
            print("Warning low uploading speed")

if __name__ == "__main__":
    oo = speedtest_bot()
    oo.check_internet_speed()

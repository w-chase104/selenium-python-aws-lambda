from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time



def lambda_handler(event, context):
    # TODO implement
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

    driver = webdriver.Chrome(chrome_options=chrome_options)
    page_data = ""
    driver.get(
        "https://salescenter.deere.com/HAResultList?serviceBeanName=thServiceAllComponents&runTest=true&resultFormat=xml")
    for i in range(60):
        try:
            if driver.find_element_by_xpath(
                    "(.//*[normalize-space(text()) and normalize-space(.)='Sales Center'])[1]/following::span[1]").is_displayed(): break
        except:
            pass
        time.sleep(1)
    else:
        return("time out")
    driver.get(
        "https://salescenter.deere.com/HAResultList?serviceBeanName=thServiceAllComponents&runTest=true&resultFormat=xml")
    time.sleep(3)
    page_data = driver.page_source
    driver.close()
    return page_data

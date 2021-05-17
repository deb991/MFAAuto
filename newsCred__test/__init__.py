__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

import logging
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\\Users\\Debashis.D.Biswas\\Documents\\pkgs\\chromedriver\\chromedriver.exe")
browser.get("https://app.welcomesoftware.com/cloud/settings/userManagement")
browser.maximize_window()


os.chdir("..\\log")
logging.basicConfig(filename = "newsCredLog.txt", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

def usrOps():
    #pass
    #print("Session start @ ", strftime("%m-%d-%y, %H-%M-%S"))
    mailInput = browser.find_element_by_class_name("form-control")
    logging.debug("element-find: {}".format(mailInput))
    mailInput.send_keys("debashis.d.biswas@shell.com")

    #enterButt =
    browser.find_element_by_xpath("/html/body/section/main/div/form/div[2]/button").send_keys(Keys.ENTER)





#browser.quit()

if __name__ == '__main__':
    usrOps()
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os

options = Options()
service = Service(log_path=os.devnull)
browser = webdriver.Firefox(options=options, service=service)

browser.get(f"https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&ifkv=AYZoVhfmpd5NXmdJXTNa2OihBFkZmVa7FXMd5kxNEwF45AAsJYXGhlayxdxHJ7qemSrCScqZf2fx1A&service=accountsettings&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1290950379%3A1695814398778473&theme=glif")

mailInput = browser.find_element(By.ID, "identifierId")
mailInput.send_keys("mail@gmail.com")
mailInput.send_keys(Keys.ENTER)
sleep(3)

passInput = browser.find_element(By.NAME, "Passwd")
passInput.send_keys("password")
passInput.send_keys(Keys.ENTER)
sleep(10)
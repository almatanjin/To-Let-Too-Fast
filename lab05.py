from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path="C:\\Users\\ASUS-PC\\PycharmProjects\\selenium-nazia\\drivers\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.current_url)

driver.find_element(By.NAME, "txtUsername").send_keys("Admin")

print("find username field\n")

driver.find_element(By.ID, "txtPassword").send_keys("admin123")

print("find password field\n")

time.sleep(2)

driver.find_element(By.ID, "btnLogin").click()

print("find login field\n")

driver.close()
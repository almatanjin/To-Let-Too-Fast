from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path="C:\\Users\\ASUS-PC\\PycharmProjects\\selenium-nazia\\drivers\\chromedriver.exe")

driver.get("http://127.0.0.1:8000/accounts/login/")

print(driver.current_url)

driver.find_element_by_id('id_username').send_keys("naziatabassum")

print("find username field\n")

driver.find_element_by_id('id_password').send_keys("nazianazia")

print("find password field\n")

time.sleep(2)

driver.find_element_by_id('login_id').click()

print("find username field\n")



driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()

print("After Logout ", driver.current_url)

assert "login" in driver.current_url

driver.close()
from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path="C:\\Users\\ASUS-PC\\PycharmProjects\\selenium-nazia\\drivers\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.current_url)

driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")

print("find username field\n")

driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("admin123")

print("find password field\n")

time.sleep(2)

driver.find_element(By.XPATH, "//input[@value='LOGIN']").click()

print("find username field\n")

driver.find_element(By.XPATH,"//a[contains(text(),'Welcome')]").click()

print("find welcome text \n")

time.sleep(2)

driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()

print("After Logout ", driver.current_url)

assert "login" in driver.current_url

driver.close()
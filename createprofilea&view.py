from selenium import webdriver
import time
USERNAME='ssalma'
PASSWORD='salmasalmasalmasalma'

driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:8000/create-profile/")
userinput=driver.find_element_by_id('id_username')
userinput.send_keys(USERNAME)
passwordinput=driver.find_element_by_id('id_password')
passwordinput.send_keys(PASSWORD)
login_button=driver.find_element_by_id('login_id')
login_button.click()
driver.find_element_by_name('profile_picture').send_keys("C://Users/ALMA TANJIN/PycharmProjects/Selenium01p/media/almapic.JPG")
driver.find_element_by_name('contact_no').send_keys('8801990777777')
driver.find_element_by_name('name').send_keys('Alma Tanjin')
driver.find_element_by_name('email').send_keys('alma.88@gmail.com')
button=driver.find_element_by_id('id')
button.click()
driver.get("http://127.0.0.1:8000/view-profile/")


time.sleep(10)
driver.close()

print("succesful")
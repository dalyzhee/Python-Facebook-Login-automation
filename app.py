from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from getpass4 import getpass

# email = input("Enter email: ")
# password = getpass("Enter password: ")
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login/")
print("Facebook opened")
sleep(1)

user_email = driver.find_element(By.ID, 'email_container')
user_email.send_keys("levis123@gmail.com")
print("Email Entered")
sleep(1)
user_password = driver.find_element(By.ID, 'pass')
user_password.send_keys("levis123")
print("Password Entered")

login = driver.find_element(By.ID, 'loginbutton')
login.click()

print("Done")
input("Enter any key to quit")
driver.quit()
print("finished")
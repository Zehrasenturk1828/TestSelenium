from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Sauce:

     def test_empty_username_password(self):
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get("https://www.saucedemo.com./")
         sleep(3)
         userNameInput = driver.find_element(By.ID,"user-name")
         passwordInput = driver.find_element(By.ID,"password")
         sleep(2)
         userNameInput.send_keys("")
         passwordInput.send_keys("")
         sleep(2)
         loginButton = driver.find_element(By.ID,"login-button")
         loginButton.click()
         sleep(2)
         errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
         print(errorMessage.text)
         testResult = errorMessage.text == "Epic sadface: Username is required"
         print(f"TEST SONUCU: {testResult}")

     def test_empty_password(self):
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get("https://www.saucedemo.com./")
         sleep(3)
         userNameInput = driver.find_element(By.ID,"user-name")
         passwordInput = driver.find_element(By.ID,"password")
         sleep(2)
         userNameInput.send_keys("1")
         passwordInput.send_keys("")
         sleep(2)
         loginButton = driver.find_element(By.ID,"login-button")
         loginButton.click()
         sleep(2)
         errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
         print(errorMessage.text)
         testResult = errorMessage.text == "Epic sadface: Password is required"
         print(f"TEST SONUCU: {testResult}")
    
     def test_user_locked_out(self):
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get("https://www.saucedemo.com./")
         sleep(3)
         userNameInput = driver.find_element(By.ID,"user-name")
         passwordInput = driver.find_element(By.ID,"password")
         sleep(2)
         userNameInput.send_keys("locked_out_user")
         passwordInput.send_keys("secret_sauce")
         sleep(2)
         loginButton = driver.find_element(By.ID,"login-button")
         loginButton.click()
         sleep(2)
         errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
         print(errorMessage.text)
         testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
         print(f"TEST SONUCU: {testResult}")

     def test_valid_login(self):
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get("https://www.saucedemo.com./")
         sleep(3)
         userNameInput = driver.find_element(By.ID,"user-name")
         passwordInput = driver.find_element(By.ID,"password")
         sleep(2)
         userNameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")
         sleep(2)
         loginButton = driver.find_element(By.ID,"login-button")
         loginButton.click()
         sleep(4)
         url = "https://www.saucedemo.com./inventory.html"
         if driver.current_url == url:
              print("url doğru")
         else:
            print("yanlış url")
         box = driver.find_elements(By.CLASS_NAME,"inventory_item")
         sleep(5)
         print(f"saucedemo sitesinde şu anda {len(box)} adet ürün vardır.")

        



testClass = Test_Sauce()
testClass.test_empty_username_password()
testClass.test_empty_password()
testClass.test_user_locked_out()
testClass.test_valid_login()

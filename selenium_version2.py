from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os


chromedriver_path = "C:\\BUI_HUYEN\\Driver\\chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:80/TP_Javascrip_selenium_projet/Javascrip_selenium_projet/form_version2.php")
driver.maximize_window()


test = ["Florent1", "Bailly", "Huy" ,  "11 rue de it 69000 Lyon", "123", "Huyen", "00001111", "9/24" , "zip" ]


driver.find_element(By.ID, "firstName").send_keys(test[0])
time.sleep(0.5)
driver.find_element(By.ID, "lastName").send_keys(test[1])
time.sleep(0.5)
driver.find_element(By.ID, "username").send_keys(test[2])
time.sleep(0.5)
driver.find_element(By.ID, "address").send_keys(test[3])
time.sleep(1)

time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="country"]/option[2]').click()

time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="state"]/option[2]').click()

time.sleep(0.5)
driver.find_element(By.ID, "zip").send_keys(test[4])

time.sleep(0.5)
driver.find_element(By.ID, "cc-name").send_keys(test[5])


time.sleep(0.5)
driver.find_element(By.ID, "cc-number").send_keys(test[6])

time.sleep(0.5)
driver.find_element(By.ID, "cc-expiration").send_keys(test[7])

time.sleep(0.5)
driver.find_element(By.ID, "cc-cvv").send_keys(test[8]) 

time.sleep(0.5)
driver.execute_script("document.getElementById('details').value= 'le champs est renseigné';")

time.sleep(0.5)

buttonContinue = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.btn-block")
driver.execute_script("arguments[0].click();", buttonContinue)

# element = driver.find_element(By.ID, "submitForm")
# driver.execute_script("arguments[0].click();", element)

log_directory = os.path.join(os.getcwd(), 'LOG')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_path = os.path.join(log_directory, 'log.txt')
with open(log_path, 'a') as log_file:
        log_file.write(f"Test failed with error: \n")

input() 




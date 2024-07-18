from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# Open the Google form
driver.get('https://forms.gle/WT68aV5UnPajeoSc8')

# Wait for the page to load completely
time.sleep(5)

# Fill out the form fields
# Example XPaths - Update these based on your form structure
Full_name_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input' 
phone_number_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
email_xpath = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
Pin_code_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
DOB_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
Gender_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'
submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'

# Fill the "Name" field
name_field = driver.find_element(By.XPATH, Full_name_xpath)
name_field.send_keys('Aakash Gandhi')


# Fill the "Contact Number" field
phone_number_field = driver.find_element(By.XPATH, phone_number_xpath)
phone_number_field.send_keys('123456789')

# Fill the "Email" field
email_field = driver.find_element(By.XPATH, email_xpath)
email_field.send_keys('aakashgandhi622@gmail.com')


address_field = driver.find_element(By.XPATH, address_xpath)
address_field.send_keys('ABC')

Pin_code_Field = driver.find_element(By.XPATH, Pin_code_xpath)
Pin_code_Field.send_keys('123456')

DOB_Field = driver.find_element(By.XPATH, DOB_xpath)
DOB_Field.send_keys('01-01-2000')


Gender_Field = driver.find_element(By.XPATH, Gender_xpath)
Gender_Field.send_keys('Male')



# Locate the verification code text and extract it
verification_text_xpath = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[1]/div/div[1]/span[1]'
verification_code_element = driver.find_element(By.XPATH, verification_text_xpath)
verification_code = verification_code_element.text.split(': ')[1].replace('<b>', '').replace('</b>', '').strip()
# Fill the verification code field
verification_code_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'
verification_code_field = driver.find_element(By.XPATH, verification_code_field_xpath)
verification_code_field.send_keys(verification_code)



# Submit the form
submit_button = driver.find_element(By.XPATH, submit_button_xpath)
submit_button.click()

# Wait for the confirmation page to load
time.sleep(5)

screenshot_path = 'D:/form_ss/confirmation_page.png'
driver.save_screenshot(screenshot_path)

# Close the browser
driver.quit()

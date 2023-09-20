from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


# Replace this URL with your Google Form URL
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSd25l04kdkF5N7L2tY9ApfZHkSW6lnGyuU9rdhjNalu_kaUPQ/viewform?fbclid=IwAR1TVC52qx2PMM3xXG4jQs4TTCERpagJdBuh2PRVrx_l8FrCuVVKj2XTtn8"
with open('data.csv', 'r') as f:
    input_data = f.readlines()

# Create a web driver instance with a Service object
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def fill_form():
    driver.get(form_url)
    time.sleep(1)  # Wait for the form to load

    for element in input_data:
        print(element)
        if ('_' in element):
            xpath = element.split('_')[0]
            input_text = element.split('_')[1]
            curr_element = driver.find_element(By.XPATH, xpath)
            curr_element.send_keys(input_text)
        else:
            curr_element = driver.find_element(By.XPATH, element)
            curr_element.click()
        time.sleep(0.15)


for i in range(30):
    fill_form()
    time.sleep(1)

# Close the browser
driver.quit()

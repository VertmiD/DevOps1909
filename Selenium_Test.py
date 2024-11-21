from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path to the ChromeDriver
driver_path = 'C:\\Windows\\System32\\chromedriver.exe'  # Adjust the path if needed
my_service = Service(driver_path)

driver = webdriver.Chrome(service=my_service)

# Open a webpage
driver.get("http://www.ynet.co.il")

# Print the title of the webpage
print(driver.title)
print(driver. current_url)

# Close the browser
driver.quit()
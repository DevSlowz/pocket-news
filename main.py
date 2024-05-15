from selenium import webdriver
from selenium.webdriver.common.by import By

def main ():

    # Navigate to Yahoo Finance
    # Locate the search bar
    # Search for the user specified stock symbol - We will need to determine if the symbol is valid somehow
    # Load the stock specfic page
    # Scrape the stock price at the current time 
    # Scrape the first 3 videos that appear in the all section
    driver = webdriver.Chrome()

    driver.get("https://ca.finance.yahoo.com/quote/GME")

    title = driver.title

    driver.implicitly_wait(0.10)

    # text_box = driver.find_element(by=By.NAME, value="my-text")
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # text_box.send_keys("Selenium")
    # submit_button.click()

    # message = driver.find_element(by=By.ID, value="message")
    # text = message.text

    driver.quit()
    print(title)

main()
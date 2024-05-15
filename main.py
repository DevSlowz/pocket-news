from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def main ():

    # Navigate to Yahoo Finance
    # Locate the search bar
    # Search for the user specified stock symbol - We will need to determine if the symbol is valid somehow
    # Load the stock specfic page
    # Scrape the stock price at the current time 
    # Scrape the first 3 videos that appear in the all section
    driver = webdriver.Chrome()

    driver.get("https://ca.finance.yahoo.com/")

    title = driver.title

    driver.implicitly_wait(0.10)
    stock_symbol = 'GME'
    # Search Bar
    search_bar = driver.find_element(By.ID ,"yfin-usr-qry")
    # Search for user inputed stock symbol/tick and direct automation to page
    search_bar.send_keys(stock_symbol, Keys.ENTER)
    time.sleep(5)

    # Extract the stock price
    price_element = driver.find_element(By.XPATH ,f"//fin-streamer[@data-symbol='{stock_symbol}']")
    stock_price = price_element.get_attribute("value")

    print("Stock price:", stock_price)

    # Extract the Price-to-Earnings (P/E) Ratio
    price_to_earning = driver.find_element( By.XPATH,"//td[@data-test='PE_RATIO-value']")
    print("P/E:", price_to_earning.text)
    # text_box.send_keys("Selenium")
    # submit_button.click()

    # message = driver.find_element(by=By.ID, value="message")
    # text = message.text

    driver.quit()
    print(title)

main()
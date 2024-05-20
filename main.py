from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def main ():

    main_menu_option = ""

    # Welcome Message
    print("Welcom to Pocket News Your Handy Partner For Keeping Track Of Stocks.")

    # Determin what user wants to do
    # 1. View active stats on current list of stocks
    # 2. View list of active stocks
    # 3. Remove stock Symbol
    # 4. Add stock symbol

    main_menu_option = input('''Please enter an option: \n 
1. View active stats on current list of stocks \n 
2. View list of active stocks \n 
3. Remove stock Symbol \n 
4. Add stock symbol \n 
Option: ''')

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
    stock_symbol = 'FFIE'
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

    # Extract the Earnings Per Share (EPS)
    earning_per_share = driver.find_element( By.XPATH,"//td[@data-test='EPS_RATIO-value']")
    print("EPS:", earning_per_share.text)

    # Extract the Dividend Yield
    dividend_yield = driver.find_element( By.XPATH,"//td[@data-test='DIVIDEND_AND_YIELD-value']")
    print("Dividend Yield:", dividend_yield.text)

    # Extract the Market Cap
    market_cap = driver.find_element( By.XPATH,"//td[@data-test='MARKET_CAP-value']")
    print("Market Cap:", market_cap.text)

    # Navigate to the Statisitics page
    driver.find_element( By.XPATH,'//*[@id="quote-nav"]/ul/li[4]/a').click()
    time.sleep(2)

    # Extract the Debt-to-Equity Ratio
    doe_ratio = driver.find_element( By.XPATH, '//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[3]/div/div[5]/div/div/table/tbody/tr[4]/td[2]')
    print("Debt-to-Equity Ratio:", doe_ratio.text)
    


    # text_box.send_keys("Selenium")
    # submit_button.click()

    # message = driver.find_element(by=By.ID, value="message")
    # text = message.text

    driver.quit()
    print(title)

main()
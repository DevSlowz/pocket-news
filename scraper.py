# Scraper libraries 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait

class StockScraper:

    # def __init__(self):
    #     pass

    def collect_stock_stats(self, symbol):
        driver = webdriver.Chrome()

        driver.get("https://ca.finance.yahoo.com/")

        title = driver.title

        driver.implicitly_wait(0.10)
        stock_symbol = symbol
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

    def collect_articles(self, symbol) :
        driver = webdriver.Chrome()

        driver.get(f"https://ca.finance.yahoo.com/quote/{symbol}")

        li_items = driver.find_element(By.ID, "quoteNewsStream-0-Stream")
        ul_element = li_items.find_element(By.TAG_NAME, "ul")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")

        for idx, li_item in enumerate(li_elements):
            if idx >= 5:  
                break
            link_element = li_item.find_element(By.TAG_NAME, "a")
            hyperlink = link_element.get_attribute("href")
            # Ensure to strip leading/trailing whitespace
            title = link_element.text.strip()  
            if title:  # Check if title is not empty
                print("Title:", title)
                print("Hyperlink:", hyperlink)
                print()

        # Close the driver
        driver.quit()


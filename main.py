from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from stocks import Stock, read_stock_symbols
from scraper import StockScraper
import time
def main ():

    main_menu_option = ""
    scraper = StockScraper()
    exit = False
    # Welcome Message
    print("Welcom to Pocket News Your Handy Partner For Keeping Track Of Stocks.")



    while exit == False:
        main_menu_option = input('''
Please enter an option: 
1. View active stats on current list of stocks 
2. View list of active stocks 
3. Remove stock Symbol 
4. Add stock symbol 
Option: ''')
    
        if main_menu_option == "1":
            pass

    
        elif main_menu_option == "4" :
            add_symbol = ""
            add_symbol = input("Please enter valid symbol you would like to add: ")
            stock = Stock(add_symbol, 0, 0, 0, 0, 0, 0) 
            stock.add_stock(add_symbol)
            # Initialize Stock instance
            
            # stock.add_stock(add_symbol)
            # scraper.collect_articles(add_symbol)
        



main()
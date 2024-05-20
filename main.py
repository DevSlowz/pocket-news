from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from stocks import Stock, read_stock_symbols
from scraper import StockScraper
import time
import os
def main ():

    main_menu_option = ""
    scraper = StockScraper()
    exit = False
    # Welcome Message
    print("Welcom to Pocket News Your Handy Partner For Keeping Track Of Stocks.")



    while exit == False:
        main_menu_option = input('''
Please enter an option: 
1. View list of active stocks 
2. Remove stock Symbol 
3. Add stock symbol 
Option: ''')
    
        if main_menu_option == "1":
            stocks = read_stock_symbols("stock_list.txt")
            print(stocks)
            menu_option = input("1. View stats for all \n2. View stat for specific stock\nOption: ")
            if menu_option == "1":
                # Logic for generating report
                pass
            elif menu_option == "2":
                stock_option = input("Please enter valid stock symbol from list: ")
                if stock_option in stocks:
                    stock = Stock(stock_option, 0, 0, 0, 0, 0, 0) 
                    stock.display_stock(stock_option)
                    
            else:
                print("invalid option. Please try again")
                os.system('cls')


    
        elif main_menu_option == "4" :
            add_symbol = ""
            add_symbol = input("Please enter valid symbol you would like to add: ")
            stock = Stock(add_symbol, 0, 0, 0, 0, 0, 0) 
            stock.add_stock(add_symbol)
            # Initialize Stock instance
            
            # stock.add_stock(add_symbol)
            # scraper.collect_articles(add_symbol)
        



main()
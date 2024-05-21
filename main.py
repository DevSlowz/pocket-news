from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from stocks import Stock, read_stock_symbols
from scraper import StockScraper
from stocks import Report
import time
import os
def main ():

    main_menu_option = ""
    exit = False
    # Welcome Message
    print("Welcom to Pocket News Your Handy Partner For Keeping Track Of Stocks.")



    while exit == False:
        main_menu_option = input('''
Please enter an option: 
1. View list of active stocks 
2. Add stock symbol 
3. Remove stock Symbol 
Option: ''')
    
        if main_menu_option == "1":
            stocks = read_stock_symbols("stock_list.txt")
            print(stocks)
            # Main menu option 1 internal menu
            menu_option = input("1. View stats for all \n2. View stat for specific stock\nOption: ")
            if menu_option == "1":

                for stock in stocks:
                    stock_info = Stock(stock)
                    scrapper = StockScraper(stock_info)
                    scrapper.collect_stock_stats(stock_info.stock_symbol)
                    scrapper.generate_report(Stock(stock))
               
            elif menu_option == "2":
                stock_option = input("Please enter valid stock symbol from list: ")
                if stock_option in stocks:
                    stock = Stock(stock_option, 0, 0, 0, 0, 0, 0) 
                    stock.display_stock(stock_option)
                    
            else:
                print("invalid option. Please try again")
                os.system('clear')

        elif main_menu_option == "2":            
            add_symbol = input("Please enter a valid symbol you would like to add: ")
            stock = Stock(add_symbol)
            scrapper = StockScraper(add_symbol)
            try:
                # Check if the symbol is valid
                if scrapper.is_valid(add_symbol):
                    # If the symbol is valid, add it
                    stock.add_stock(add_symbol)
                else:
                    # If the symbol is not valid, print an error message
                    print("Invalid Stock Symbol")
            except Exception as e:
                # Handle any other exceptions
                print("Error:", e)

             
            
            # Initialize Stock instance

    
        elif main_menu_option == "3" :
            stock_list = read_stock_symbols("stock_list.txt")
            print(stock_list)
            remove_symbol = ""
            remove_symbol = input("Please enter valid symbol you would like to remove: ")
            stock = Stock(remove_symbol) 
            stock.remove_stock(remove_symbol)
            
            # stock.add_stock(add_symbol)
            # scraper.collect_articles(add_symbol)

        else:
            print("invalid option...Closing program")
            exit = True
        



main()
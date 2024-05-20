from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from stocks import Stock
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
    
    if main_menu_option == "4" :
        stock = Stock("AAPL", 0, 0, 0, 0, 0, 0)  # Initialize Stock instance
        add_symbol = ""
        add_symbol = input("Please enter valid symbol you would like to add: ")
        stock.add_stock(add_symbol)



main()
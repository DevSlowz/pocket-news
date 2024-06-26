from scraper import StockScraper

class Stock:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.stock_price = None
        self.price_to_earning = None
        self.earning_per_share = None
        self.dividend_yield = None
        self.market_cap = None
        self.doe_ratio = None
        # self.stock_list = []



    def display_stocks(self):
        pass

    def display_stock(self, symbol):
        scraper = StockScraper()
        scraper.collect_stock_stats(symbol)

    def add_stock(self, symbol):
        # scraper = StockScraper()
        # scraper.collect_stock_stats(symbol)
        file = open("stock_list.txt", "a")
        file.write(f"{symbol}\n")

    
    def remove_stock(self, symbol):
        with open("stock_list.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                #remove leading/trailing whitespace, including newline characters
                if i.strip() != symbol:  
                    f.write(i)
            f.truncate()


# Contain logic to generate a report on stocks
class Report:

    @staticmethod
    def generate_report(stock):
        pass




# Contain Logic for getting stocks from list

def read_stock_symbols(filename):
    try:
        with open(filename, 'r') as file:
            return[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Stock symbols file no foound")
        return []
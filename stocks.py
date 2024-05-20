class Stock:
    def __init__(self, stock_symbol, stock_price, price_to_earning, earning_per_share,
                 dividend_yield, market_cap, doe_ratio):
        self.stock_symbol = stock_symbol
        self.stock_price = stock_price
        self.price_to_earning = price_to_earning
        self.earning_per_share = earning_per_share
        self.dividend_yield = dividend_yield
        self.market_cap = market_cap
        self.doe_ratio = doe_ratio
        self.stock_list = []



    def display_stocks(self):
        pass

    def add_stock(self, symbol):
        pass

    def remove_stock(self, symbol):
        pass


# Contain logic to generate a report on stocks
class Report:
    def __init__(self):
        pass
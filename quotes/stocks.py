class StockAPI():
    def __init__(self, company_name, stock_price, prev_close, change, market_cap):
        self.company_name = company_name
        self.stock_price = stock_price
        self.prev_close = prev_close
        self.change = change
        self.market_cap = market_cap
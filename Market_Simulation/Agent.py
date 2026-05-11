
#handles agents,
#add specialized agents that work in special environments
#to make more complex, with multiple markets
class Buyer():

    def __init__(self, buyer_id, reservation_price):
        self.price = None
        self.buyer_id = buyer_id
        self.reservation_price = reservation_price
        self.trade_log = []

    def buy(self, price):
        self.price = price
        if self.reservation_price >= self.price:
            return True
        else:
            return False

    def record_trade_log(self, price):
          self.trade_log.append(price)

    def update_reservation_price(self, price):
        self.reservation_price = self.reservation_price * 0.95 + price * 0.05

    def __repr__(self):
        return str(self.buyer_id) + ":" + str(self.trade_log)

class Seller():

    def __init__(self, seller_id, reservation_price):
        self.seller_id = seller_id
        self.reservation_price = reservation_price
        self.price = None
        self.trade_log = []

    def sell(self, price):
        self.price = price
        if self.reservation_price <= self.price:
            return True
        else:
            return False

    def record_trade_log(self, price):
            self.trade_log.append(price)

    def update_reservation_price(self, price):
        self.reservation_price = self.reservation_price * 0.95 + price * 0.05

    def __repr__(self):
        return str(self.seller_id) + ":" + str(self.trade_log)

import random

class Market():
    def __init__(self, buyers, sellers):
        self.buyers = buyers
        self.sellers = sellers
        self.trades = []

    @staticmethod
    def _negotiate(buyer, seller):
        sume = buyer.reservation_price + seller.reservation_price
        midpoint = sume/2
        if buyer.buy(midpoint) and seller.sell(midpoint):
            return buyer.price
        return None

    def run_round(self, round_number):
        random.shuffle(self.buyers)
        random.shuffle(self.sellers)

        round_buy = []

        for buyer, seller in zip(self.buyers, self.sellers):
            trade = self._negotiate(buyer, seller)
            if trade is not None:

                buyer.record_trade_log(trade)
                seller.record_trade_log(trade)

                buyer.update_reservation_price(trade)
                seller.update_reservation_price(trade)

                round_buy.append(trade)
                self.trades.append({"round": round_number, "price": trade})
        return round_buy

    def equilibrium(self):
        if not self.trades:
            return None
        price_avg = sum([i["price"] for i in self.trades]) / len(self.trades)
        return price_avg


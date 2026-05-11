import csv

from Market import *
from Agent import *
import random
import csv

def generate_buyers(n, mean_price, dev_instance):
    buyers = []
    for i in range(n):
        price = max(1, random.gauss(mean_price, dev_instance))
        buyer = Buyer(i, round(price, 2))
        buyers.append(buyer)
    return buyers

def generate_sellers(n, mean_price, dev_instance):
    sellers = []
    for i in range(n):
        price = max(1, random.gauss(mean_price, dev_instance))
        seller = Seller(i, round(price, 2))
        sellers.append(seller)
    return sellers

def run_simulation(config: dict ):
    random.seed(config.get("seed"))

    buyers = generate_buyers(config["num_buyers"], config["buyer_mean_price"], config["dev_instance"])
    sellers = generate_sellers(config["num_sellers"], config["seller_mean_price"], config["dev_instance"])
    market = Market(buyers, sellers)

    round_data = []
    for round_num in range(1, config["rounds"] + 1):
        if round_num == config["shock_round"]:
            for seller in sellers:
                seller.reservation_price *= config["shock_magnitude"]

        trade_run = market.run_round(round_num)

        if trade_run:
            avg_price = sum(trade_run) / len(trade_run)
            vol = len(trade_run)
        else:
            avg_price = 0
            vol = 0

        round_data.append({
            "round_num": round_num,
            "avg_price": avg_price,
            "vol": vol, })
    return {
        "trades": market.trades,
        "round_data": round_data,
        "buyers": buyers,
        "sellers": sellers,
        "average_price": market.equilibrium(),
        "config": config }

def export_trades(result, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['round', 'price'])
        writer.writeheader()
        writer.writerows(result['trades'])
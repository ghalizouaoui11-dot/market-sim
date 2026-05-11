
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec


def plot_graph(results: dict, title: str = None):

    config = results["config"]
    buyers = results["buyers"]
    sellers = results["sellers"]
    round_data = results["round_data"]
    trades = results["trades"]
    average_price = results["average_price"]

    rounds = [i["round_num"] for i in round_data]
    avg_price = [i["avg_price"] for i in round_data]
    volume = [i["vol"] for i in round_data]
    prices = [i["price"] for i in trades]

    fig = plt.figure(figsize=(14, 9))
    gs = gridspec.GridSpec(3, 1, figure=fig)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    ax3 = fig.add_subplot(gs[2])

    ax1.set_title(title)
    ax1.set_xlabel("Rounds")
    ax1.set_ylabel("Price")
    ax1.axhline(y=average_price, color='black', linestyle='--', label="Equilibrium Price")
    sns.lineplot(x=rounds, y=avg_price, ax=ax1, label="Average Price")
    ax1.legend()

    ax2.set_title("Trade Volumes per Round")
    ax2.set_xlabel("Rounds")
    ax2.set_ylabel("Volume")
    sns.lineplot(x=rounds, y=volume, ax=ax2, label="Trade Volume")
    ax2.legend()

    ax3.set_title("Trade Price Distribution")
    ax3.set_ylabel("Count")
    ax3.set_xlabel("Reservation Price")
    ax3.legend()

    buyer_prices = [i.reservation_price for i in buyers]
    seller_prices = [i.reservation_price for i in sellers]
    sns.histplot(buyer_prices, ax=ax3, label="Buyer Prices", color='blue', alpha=0.6)
    sns.histplot(seller_prices, ax=ax3, label="Seller Prices", color='red', alpha=0.6)
    ax3.legend()
    fig.tight_layout()
    plt.show()



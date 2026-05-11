import logging

from Sim_Engine import *
from Visuals import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
file_handler = logging.FileHandler("Market_Simulation.log", mode="w", encoding="utf-8", delay=True)
handler.setFormatter(formater)
file_handler.setFormatter(formater)
logger.addHandler(handler)
logger.addHandler(file_handler)



CONFIG = {
    "seed": 42,
    "num_buyers": 51,
    "num_sellers": 49,
    "buyer_mean_price": 110,
    "seller_mean_price": 90,
    "dev_instance": 15,
    "rounds": 50,
    "plot_results": True,
    "shock_round": 25,
    "shock_magnitude": 1.2
    }


if __name__ == "__main__":
    print("Simulation Configuration:")
    logger.info(f"Simulation Configuration: {CONFIG}")
    print(CONFIG)
    print("Simulation Results:")
    print("==================")
    results = run_simulation(CONFIG)
    logger.info(f"Simulation Results: total trades: {len(results['trades'])}, average price: {results['average_price']:.2f}, theoretical midpoint: {((CONFIG['buyer_mean_price'] + CONFIG['seller_mean_price']) / 2):.2f}")

    print(f"total trades: {len(results['trades'])}")
    print(f"Estimated equilibrium: {results['average_price']:.2f}")
    print(f"theoretical midpoint: {((CONFIG['buyer_mean_price'] + CONFIG['seller_mean_price']) / 2):.2f}")

    if CONFIG["plot_results"]:
        plot_graph(results, title="Market Simulation Results")
        logger.info("Graph plotted")

    export_trades(results, "trades.csv")
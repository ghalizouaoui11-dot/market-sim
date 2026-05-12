# Agent-Based Market Simulation
A Python simulation of a double auction market using agent-based modelling,
a methodology widely used in computational economics research.

## how it works
Buyers and sellers each have a reservation price — the maximum a buyer will
pay, or the minimum a seller will accept. Each round, agents are randomly
paired. If a mutually acceptable price exists, a trade executes at the
midpoint of their reservation prices. Over many rounds, the average trade
price converges toward the theoretical market equilibrium.

Agents use adaptive expectations — after each trade, they adjust their
reservation price toward the observed trade price, modelling learning
behaviour in real markets.

A supply shock can be introduced at a specified round, shifting all seller
reservation prices up by a configurable magnitude. This model's real economic
events, such as supply chain disruptions or sudden cost increases.

## project structure
| File | Purpose |
| `Agent.py` | Buyer and Seller agent classes |
| `Market.py` | Matching mechanism and trade logic |
| `Sim_Engine.py` | Agent generation and simulation runner |
| `Visuals.py` | Matplotlib/Seaborn output |
| `Config.py` | Entry point and configuration |

## How to run
must be run on Python
"bash python Config.py"

## Configuration
| Parameter | Default | Description |
|---|---|---|
| `num_buyers` | 51 | Number of buyer agents |
| `num_sellers` | 49 | Number of seller agents |
| `buyer_mean_price` | 110 | Mean buyer reservation price |
| `seller_mean_price` | 90 | Mean seller reservation price |
| `dev_instance` | 15 | Standard deviation of reservation prices |
| `rounds` | 50 | Trading rounds to simulate |
| `shock_round` | 25 | Round at which supply shock occurs |
| `shock_magnitude` | 1.2 | Multiplier applied to seller reservation prices |

## Experiment to try
- Set `shock_magnitude` to 1.3 — volume collapses and average price
  paradoxically drops as only lowest-cost sellers remain viable
- Increase `dev_instance` to 30 — more agent heterogeneity, observe
  effect on convergence speed
- Remove adaptive expectations — compare convergence with and without
  agent learning

## Reference
Smith, V. L. (1962). An Experimental Study of Competitive Market Behavior.
*Journal of Political Economy*, 70(2), 111–137.


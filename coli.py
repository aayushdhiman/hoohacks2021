import json

# Cost of living indices from https://worldpopulationreview.com/state-rankings/cost-of-living-index-by-state
# Annual expenditures from https://www.statista.com/statistics/247407/average-annual-consumer-spending-in-the-us-by-type/
# and https://www.nationwide.com/lc/resources/personal-finance/articles/average-cost-of-utilities

coli = json.loads(open("coli.json", 'r').read())

average_costs = {
    "grocery": 8169,
    "housing": 20679,
    "utilities": 2060,
    "transportation": 10742,
    "misc": 4941
}

def get_state_cost(state, category):
    return average_costs[category] - average_costs[category] * ((100 - float(coli[state][f"{category}Cost"])) / 100)

# average_whatever - average_whatever * ((100 - index) / 100)

if __name__ == "__main__":
    print(get_state_cost("Virginia", "housing"))

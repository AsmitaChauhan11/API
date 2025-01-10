# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Product details with their respective centers and weights
# products = {
#     "A": {"center": "C1", "weight": 3},
#     "B": {"center": "C1", "weight": 2},
#     "C": {"center": "C1", "weight": 8},
#     "D": {"center": "C2", "weight": 12},
#     "E": {"center": "C2", "weight": 25},
#     "F": {"center": "C2", "weight": 15},
#     "G": {"center": "C3", "weight": 0.5},
#     "H": {"center": "C3", "weight": 1},
#     "I": {"center": "C3", "weight": 2}
# }

# # Distance matrix between centers and L1
# distances = {
#     "C1": {"L1": 3, "C2": 4, "C3": float('inf')},
#     "C2": {"L1": 2.5, "C1": 4, "C3": 3},
#     "C3": {"L1": 2, "C2": 3, "C1": float('inf')},
#     "L1": {"C1": 3, "C2": 2.5, "C3": 2}
# }

# # Cost per unit distance based on weight
# cost_per_unit = {
#     "0-5": 10,
#     "additional_5": 8
# }

# def calculate_cost(weight, distance):
#     """Calculate the cost for a given weight and distance."""
#     if weight <= 5:
#         cost_per_km = cost_per_unit["0-5"]
#     else:
#         extra_weight = weight - 5
#         extra_cost = ((extra_weight // 5) + (1 if extra_weight % 5 > 0 else 0)) * cost_per_unit["additional_5"]
#         cost_per_km = cost_per_unit["0-5"] + extra_cost
#     return cost_per_km * distance

# @app.route('/calculate-cost', methods=['POST'])
# def calculate_delivery_cost():
#     data = request.json
#     total_cost = 0
#     trips = {}  # Track products picked up from each center

#     # Step 1: Organize products by center
#     for product, quantity in data.items():
#         if product in products and quantity > 0:
#             product_center = products[product]["center"]
#             product_weight = products[product]["weight"] * quantity
#             if product_center not in trips:
#                 trips[product_center] = 0
#             trips[product_center] += product_weight

#     # Step 2: Calculate the cost for each center's trip
#     for center, weight in trips.items():
#         # Trip from center to L1
#         distance_to_L1 = distances[center]["L1"]
#         total_cost += calculate_cost(weight, distance_to_L1)

#     # Step 3: Return total cost
#     return jsonify({"total_cost": total_cost})

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Product details with their respective centers and weights
# products = {
#     "A": {"center": "C1", "weight": 3},
#     "B": {"center": "C1", "weight": 2},
#     "C": {"center": "C1", "weight": 8},
#     "D": {"center": "C2", "weight": 12},
#     "E": {"center": "C2", "weight": 25},
#     "F": {"center": "C2", "weight": 15},
#     "G": {"center": "C3", "weight": 0.5},
#     "H": {"center": "C3", "weight": 1},
#     "I": {"center": "C3", "weight": 2}
# }

# # Distance matrix between centers and L1
# distances = {
#     "C1": {"L1": 3, "C2": 4, "C3": float('inf')},
#     "C2": {"L1": 2.5, "C1": 4, "C3": 3},
#     "C3": {"L1": 2, "C2": 3, "C1": float('inf')},
#     "L1": {"C1": 3, "C2": 2.5, "C3": 2}
# }

# # Fixed costs for L1 to centers
# fixed_costs = {
#     "C1": 30,
#     "C2": 25,
#     "C3": 20
# }

# # Cost per unit distance based on weight
# cost_per_unit = {
#     "0-5": 10,
#     "additional_5": 8
# }

# def calculate_cost(weight, distance):
#     """Calculate the cost for a given weight and distance."""
#     if weight <= 5:
#         cost_per_km = cost_per_unit["0-5"]
#     else:
#         extra_weight = weight - 5
#         extra_cost = ((extra_weight // 5) + (1 if extra_weight % 5 > 0 else 0)) * cost_per_unit["additional_5"]
#         cost_per_km = cost_per_unit["0-5"] + extra_cost
#     return cost_per_km * distance

# @app.route('/calculate-cost', methods=['POST'])
# def calculate_delivery_cost():
#     data = request.json
#     total_cost = 0
#     trips = {}  # Track products picked up from each center
#     centers_to_visit = []  # Track centers where products need to be picked up

#     # Step 1: Organize products by center
#     for product, quantity in data.items():
#         if product in products and quantity > 0:
#             product_center = products[product]["center"]
#             product_weight = products[product]["weight"] * quantity
#             if product_center not in trips:
#                 trips[product_center] = 0
#                 centers_to_visit.append(product_center)
#             trips[product_center] += product_weight

#     # Step 2: Process trips
#     while centers_to_visit:
#         current_center = centers_to_visit.pop(0)
#         weight = trips[current_center]
        
#         # Trip from center to L1
#         distance_to_L1 = distances[current_center]["L1"]
#         total_cost += calculate_cost(weight, distance_to_L1)

#         # Check if more centers need to be visited
#         if centers_to_visit:
#             next_center = centers_to_visit[0]
#             total_cost += fixed_costs[next_center]  # Add the fixed cost for moving from L1 to the next center

#     # Step 3: Return total cost
#     return jsonify({"total_cost": total_cost})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify

app = Flask(__name__)

# Product details with their respective centers and weights
products = {
    "A": {"center": "C1", "weight": 3},
    "B": {"center": "C1", "weight": 2},
    "C": {"center": "C1", "weight": 8},
    "D": {"center": "C2", "weight": 12},
    "E": {"center": "C2", "weight": 25},
    "F": {"center": "C2", "weight": 15},
    "G": {"center": "C3", "weight": 0.5},
    "H": {"center": "C3", "weight": 1},
    "I": {"center": "C3", "weight": 2}
}

# Distance matrix between centers and L1
distances = {
    "C1": {"L1": 3, "C2": 4, "C3": float('inf')},
    "C2": {"L1": 2.5, "C1": 4, "C3": 3},
    "C3": {"L1": 2, "C2": 3, "C1": float('inf')},
    "L1": {"C1": 3, "C2": 2.5, "C3": 2}
}

# Fixed costs for L1 to centers
fixed_costs = {
    "C1": 30,
    "C2": 25,
    "C3": 20
}

# Cost per unit distance based on weight
cost_per_unit = {
    "0-5": 10,
    "additional_5": 8
}

def calculate_cost(weight, distance):
    """Calculate the cost for a given weight and distance."""
    if weight <= 5:
        cost_per_km = cost_per_unit["0-5"]
    else:
        extra_weight = weight - 5
        extra_cost = ((extra_weight // 5) + (1 if extra_weight % 5 > 0 else 0)) * cost_per_unit["additional_5"]
        cost_per_km = cost_per_unit["0-5"] + extra_cost
    return cost_per_km * distance

@app.route('/')
def home():
    return "Welcome to the Delivery Cost Calculator API! Use the /calculate-cost endpoint."

@app.route('/calculate-cost', methods=['POST'])
def calculate_delivery_cost():
    data = request.json
    total_cost = 0
    trips = {}
    centers_to_visit = []

    for product, quantity in data.items():
        if product in products and quantity > 0:
            product_center = products[product]["center"]
            product_weight = products[product]["weight"] * quantity
            if product_center not in trips:
                trips[product_center] = 0
                centers_to_visit.append(product_center)
            trips[product_center] += product_weight

    while centers_to_visit:
        current_center = centers_to_visit.pop(0)
        weight = trips[current_center]
        
        distance_to_L1 = distances[current_center]["L1"]
        total_cost += calculate_cost(weight, distance_to_L1)

        if centers_to_visit:
            next_center = centers_to_visit[0]
            total_cost += fixed_costs[next_center]

    return jsonify({"total_cost": total_cost})

if __name__ == '__main__':
    app.run(debug=True)

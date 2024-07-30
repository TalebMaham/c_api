from stock.models import Product

products = [
    {"name": "Pommes", "price": 0.1},
    {"name": "Bananes", "price": 0.2},
    {"name": "Barre de céréales", "price": 0.5},
    {"name": "Soda", "price": 1.0},
    {"name": "Chips", "price": 2.0},
    {"name": "Cookies", "price": 0.5},
    {"name": "Bonbons", "price": 0.2},
    {"name": "Eau minérale", "price": 1.0},
    {"name": "Jus de fruits", "price": 2.0},
    {"name": "Café", "price": 1.0},
    {"name": "Thé glacé", "price": 2.0},
    {"name": "Barre énergétique", "price": 0.5},
    {"name": "Gum", "price": 0.1},
    {"name": "Crackers", "price": 0.2},
    {"name": "Salade", "price": 2.0},
    {"name": "Yaourt", "price": 1.0},
    {"name": "Smoothie", "price": 2.0},
    {"name": "Pain au chocolat", "price": 1.0},
]

for product in products:
    Product.objects.create(**product)

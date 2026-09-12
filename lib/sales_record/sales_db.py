import json
import os


def create_sales(sale):
    new_sale = {
        "item": sale.item,
        "quantity": sale.quantity,
        "price_per_unit": sale.price_per_unit,
    }
    if os.path.exists("sales_db.json") and os.path.getsize("sale_db.json") > 0:
        with open("sales_db.json", "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(new_sale)

    with open("sales_db.json", "w") as file:
        json.dump(data, file, indent=4)
        print("sale added successfuly.")


def get_all_sales():
    if os.path.exists("sales_db.json") and os.path.getsize("sales_db.json") > 0:
        with open("sales_db.json", "r") as file:
            data = json.load(file)
    else:
        data = []
    return data

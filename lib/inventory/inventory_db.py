import json
import os

from .grape_stock import GrapeStock
from .wine_batch import WineBatch


def add_inventory_item(item):
    if os.path.exists("inventory_db.json") and os.path.getsize("inventory_db.json") > 0:
        with open("inventory_db.json", "r") as file:
            data = json.load(file)
    else:
        data = {"wine": [], "grapes": []}

    if isinstance(item, WineBatch):
        data["wine"].append(
            {
                "batch_id": item.batch_id,
                "wine_type": item.wine_type,
                "vintage": item.vintage,
                "quantity": item.quantity,
            }
        )
    elif isinstance(item, GrapeStock):
        data["grapes"].append(
            {
                "grape_type": item.grape_type,
                "variety": item.variety,
                "quantity": item.quantity,
            }
        )

    with open("inventory_db.json", "w") as file:
        json.dump(data, file, indent=4)
        print("Inventory item added successfuly.")


def get_inventory_items():
    if os.path.exists("inventory_db.json") and os.path.getsize("inventory_db.json") > 0:
        with open("inventory_db.json", "r") as file:
            data = json.load(file)
    else:
        data = {"wine": [], "grapes": []}
    return data


def delete_inventory_item(item):
    if os.path.exists("inventory_db.json") and os.path.getsize("inventory_db.json") > 0:
        with open("inventory_db.json", "r") as file:
            data = json.load(file)
    else:
        print("We cant find any inventory items")
        return

    if isinstance(item, WineBatch):
        data["wine"] = [i for i in data["wine"] if i["batch_id"] != item.batch_id]
    elif isinstance(item, GrapeStock):
        data["grapes"].append({})

    with open("inventory_db.json", "w") as file:
        json.dump(data, file, indent=4)
        print("Inventory item deleted successfuly.")

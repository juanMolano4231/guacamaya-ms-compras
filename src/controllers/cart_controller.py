from flask import request, jsonify, g
from src.models.cart_model import *

def get_cart():
    cart = get_or_create_cart(g.user["id"])
    items = get_cart_items(cart["id"])
    return jsonify({"cart": cart, "items": items})

def add_item_controller():
    data = request.json
    cart = get_or_create_cart(g.user["id"])

    item = add_item(
        cart["id"],
        data["product_id"],
        data["quantity"],
        data["price_at_add"]
    )

    return jsonify(item), 201

def update_item_controller(item_id):
    data = request.json
    item = update_item(item_id, data["quantity"])
    return jsonify(item)

def delete_item_controller(item_id):
    delete_item(item_id)
    return "", 204

def get_total_controller():
    total = get_total(g.user["id"])
    return jsonify(total)

def get_all_carts_controller():
    carts = get_all_carts()
    return jsonify(carts)
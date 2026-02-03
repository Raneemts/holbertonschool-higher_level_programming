#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_products_from_json(filename):
    """Read products from a JSON file and return a list of dicts."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                products = []
                for item in data:
                    if isinstance(item, dict):
                        products.append({
                            "id": int(item.get("id")) if item.get("id") is not None else None,
                            "name": item.get("name"),
                            "category": item.get("category"),
                            "price": float(item.get("price")) if item.get("price") is not None else None
                        })
                return products
    except (FileNotFoundError, json.JSONDecodeError, ValueError, TypeError):
        return []
    return []


def read_products_from_csv(filename):
    """Read products from a CSV file and return a list of dicts."""
    products = []
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    products.append({
                        "id": int(row.get("id")) if row.get("id") else None,
                        "name": row.get("name"),
                        "category": row.get("category"),
                        "price": float(row.get("price")) if row.get("price") else None
                    })
                except (ValueError, TypeError):
                    # Skip bad rows
                    continue
    except FileNotFoundError:
        return []
    return products


@app.route('/products')
def products():
    source = request.args.get('source', '')
    id_param = request.args.get('id', None)

    # Validate source
    if source not in ('json', 'csv'):
        return render_template('product_display.html', error="Wrong source", products=[])

    # Read products based on source
    if source == 'json':
        products_list = read_products_from_json('products.json')
    else:
        products_list = read_products_from_csv('products.csv')

    # Filter by id if provided
    if id_param is not None:
        try:
            wanted_id = int(id_param)
        except ValueError:
            return render_template('product_display.html', error="Product not found", products=[])

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=[])
        return render_template('product_display.html', products=filtered, error=None)

    # No id => show all
    return render_template('product_display.html', products=products_list, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

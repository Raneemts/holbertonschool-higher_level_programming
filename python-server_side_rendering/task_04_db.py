#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_products_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            products = []
            for item in data:
                if isinstance(item, dict):
                    try:
                        products.append({
                            "id": int(item.get("id")) if item.get("id") is not None else None,
                            "name": item.get("name"),
                            "category": item.get("category"),
                            "price": float(item.get("price")) if item.get("price") is not None else None
                        })
                    except (ValueError, TypeError):
                        continue
            return products
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_products_from_csv(filename):
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
                    continue
    except FileNotFoundError:
        return []
    return products


def read_products_from_sqlite(db_filename):
    products = []
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        for r in rows:
            products.append({
                "id": int(r[0]),
                "name": r[1],
                "category": r[2],
                "price": float(r[3])
            })
    except sqlite3.Error:
        return None  # special signal for DB error
    return products


@app.route('/products')
def products():
    source = request.args.get('source', '')
    id_param = request.args.get('id', None)

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error="Wrong source", products=[])

    # Load data by source
    if source == 'json':
        products_list = read_products_from_json('products.json')
    elif source == 'csv':
        products_list = read_products_from_csv('products.csv')
    else:
        products_list = read_products_from_sqlite('products.db')
        if products_list is None:
            return render_template('product_display.html', error="Database error", products=[])

    # Filter by id if provided
    if id_param is not None:
        try:
            wanted_id = int(id_param)
        except ValueError:
            return render_template('product_display.html', error="Product not found", products=[])

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=[])
        return render_template('product_display.html', error=None, products=filtered)

    return render_template('product_display.html', error=None, products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

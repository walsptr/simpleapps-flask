from flask import Flask, render_template
import redis
import json

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379)
redis_client.set('product', json.dumps([
        {'id': 1, 'nama': 'Obeng', 'barcode': '0001', 'harga': 100},
        {'id': 2, 'nama': 'Gunting', 'barcode': '0002', 'harga': 150},
        {'id': 3, 'nama': 'Meja', 'barcode': '0003', 'harga': 300}
        ]))

items = json.loads(redis_client.get('product'))

@app.route('/')
def products_page():
    return render_template('index.html', items=items)

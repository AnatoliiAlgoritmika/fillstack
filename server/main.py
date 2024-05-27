from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*" : {"origins":'http://127.0.0.1:5500'}})

def load_data():
    try:
        with open('db.json', 'r') as file:
            data = json.load(file)
    except:
        data = []
        with open('db.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    return data

def save_data(data):
    with open('db.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    return """ Добро пожаловать на сайт Api Server TODO <br>
    1. <a href="/api/items">/api/items</a> <br>
    2. <a href="/api/items/1">/api/items/1</a> <br>
    """

@app.route('/api/items', methods=['GET'])
def get_all_items():
    data = load_data()
    return jsonify({'status': 200, 'data': data})


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    data = load_data()
    try:
        item = data[item_id]
        if item:
            return item
    except:
        return jsonify({'message': 'Item not found'})
    

@app.route('/api/items', methods=['POST'])
def create_item():
    data = load_data()
    new_item = request.json
    last_item = data[-1]
    new_item["id"] = last_item["id"] + 1
    data.append(new_item)
    save_data(data)
    # ! обязательный ответ
    return jsonify({'status': 201, 'data': data, 'message': 'Item is created'})

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    data = load_data()
    item = None
    for i in data:
        if i['id'] == item_id:
            item = i
            break
    if item:
        data.remove(item)
        save_data(data)
    else:
        return jsonify({'message': 'Item not found', 'status': 404})
    return jsonify({'status': 201, 'data': data, 'message': 'Item is deleted'})

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = load_data()
    item = None
    for i in data:
        if i['id'] == item_id:
            item = i
            break
    if item:
        item.update(request.json)
        save_data()
        return jsonify({'status': 201, 'data': data, 'message': 'Item is updated'})
    else:
        return jsonify({'message': 'Item not found', 'status': 404})

if __name__ == '__main__':
    app.run(debug=True)
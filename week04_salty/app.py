from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 1.클라이언트->서버 주문내역 저장하기
    order_name = request.form['name']
    order_number = request.form['numer']
    order_address = request.form['address']
    order_phone = request.form['phone']
    doc = {
        'name' : order_name,
        'number' : order_number,
        'address' : order_address,
        'phone' : order_phone
    }
    db.dbsparta.insert_one(doc)

    return jsonify({'result': 'success'},{'msg':'주문이 서버로 전송되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 2.서버->클라이언트 주문내역 보내주기

    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
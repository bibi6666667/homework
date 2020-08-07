from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 1.클라이언트->서버 주문내역 저장하기
    order_name = request.form['name']
    order_number = request.form['number']
    order_address = request.form['address']
    order_phone = request.form['phone']
    print(order_name, order_number, order_address, order_phone)
    doc = {
        'name' : order_name,
        'number' : order_number,
        'address' : order_address,
        'phone' : order_phone
    }
    db.order.insert_one(doc)
    return jsonify({'result': 'success','msg': '주문이 서버로 전송되었습니다!(POST)'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 2.서버->클라이언트 주문내역 보내주기
    orders = list(db.order.find({},{'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders, 'msg': '주문목록을 서버에서 불러왔습니다(GET)'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
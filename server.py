from flask import Flask, request, jsonify

app = Flask(__name__)

data_list = []

@app.route('/sensor', methods=['POST'])
def receive_data():
    data = request.json
    print("收到数据: {}".format(data))  # 改这里
    data_list.append(data)
    return jsonify({"status": "ok"})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running successfully!"

# نقطة استقبال البيانات أو الإشعارات
@app.route('/api/report', methods=['POST'])
def report_action():
    data = request.json
    feature_key = data.get("featureKey", "UNKNOWN")
    
    print(f"[ALERT] Received action flag: {feature_key}")
    
    # هنا يمكنك معالجة البيانات أو حفظها
    return jsonify({"status": "received", "code": 200})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

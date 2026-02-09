# from flask import Flask, jsonify
# from datetime import datetime

# app = Flask(__name__)

# @app.route('/health', methods=['GET'])
# def health():
#     return jsonify({
#         "status": "ok",
#         "service": "ecs-demo",
#         "timestamp": datetime.utcnow().isoformat() + "Z"
#     })

# if __name__ == '__main__':
   
#     app.run(host='0.0.0.0', port=5000)
























































from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask webapp!"


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)


# testing
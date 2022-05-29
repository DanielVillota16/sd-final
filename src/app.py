from flask import Flask, request, render_template, jsonify
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.environ['REDIS_HOST'], port=6379, password=os.environ['REDIS_PASSWORD'])

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/highest')
def highest():
    val = redis.get('highestscore')
    if not val: #if <highscore> key does not exist in redis db, create it and set it to 0
        redis.set('highestscore', 0)
    high = int(redis.get('highestscore'))
    return jsonify({"highest":high})

@app.route('/updatehighest/<score>')
def update_highest(score):
    print(request.get_data())
    status = redis.set('highestscore', int(score))
    print(">>>>", status)
    return str(status)

@app.route("/health")
def healthy():
    return "{\"message\":\"Healthy\"}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
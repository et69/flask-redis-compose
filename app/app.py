import os
import redis

from flask import Flask, jsonify

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def index():
    # Increment a counter in Redis
    counter = redis_client.incr('counter')
    return jsonify(message=f"Counter value is {counter}")

@app.route('/reset')
def reset_counter():
    redis_client.set('counter', 0)
    return jsonify(message="Counter reset")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


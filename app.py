from flask import Flask
from redis import Redis

app = Flask(__name__)
# 'redis' is the name of the other container we will create
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'''
    <div style="text-align:center; margin-top:100px; font-family:sans-serif;">
        <h1 style="color: #FF5733;">🚀 Serjojo's Traffic Monitor</h1>
        <p style="font-size: 24px;">This page has been viewed <b>{count}</b> times.</p>
        <p style="color: gray;">Database: Redis | Framework: Flask</p>
    </div>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

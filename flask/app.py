from flask import Flask
from dotenv import load_dotenv
import os
import redis

load_dotenv()

redis_URL = os.getenv("REDIS_URL")
redis_PWD = os.getenv("REDIS_PWD")
redis_PRT = os.getenv("REDIS_PRT")
redis_DBT= os.getenv("REDIS_DBT")

app = Flask(__name__)

def redis_connect():
    r = redis.Redis(host=redis_URL, 
    port=redis_PRT, 
    db=redis_DBT,
    password=redis_PWD)
    return r

@app.route('/')
def hello():
    try:
        r = redis_connect()
        print(r)
    except Exception as e:
        print("Error",e)
    return 'Hello, World'
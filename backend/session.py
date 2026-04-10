import redis
import uuid

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def create_session(email):
    token = str(uuid.uuid4())
    r.set(token, email)   # store token → email
    return token

def get_user(token):
    return r.get(token)
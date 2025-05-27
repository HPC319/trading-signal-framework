import os
import time
import jwt  # PyJWT

def create_coinbase_jwt():
    api_key_id = os.environ["COINBASE_API_KEY_ID"]
    private_key = os.environ["COINBASE_API_PRIVATE_KEY"]

    payload = {
        "iss": api_key_id,
        "sub": api_key_id,
        "aud": "coinbase-cloud",
        "iat": int(time.time()),
        "exp": int(time.time()) + 300
    }

    token = jwt.encode(payload, private_key, algorithm="ES256")
    return token

# This file is responsivle for signin, encoding, decoding and returning JWTs
import time
import jwt
from decouple import config

JWT_SECRET = "secret"

#Function returns the generated Token
def token_reponse(token: str):
    return {
        "access token" : token
    }

# Function used for signing the JWT string
def signJWT(userID : str):
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    print(token)
    return token


def decodeJWT(token : str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms="HS256")
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
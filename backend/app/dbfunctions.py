import motor.motor_asyncio
import certifi
from fastapi import HTTPException
from decouple import config
from .auth.jwtHandler import signJWT
from werkzeug.security import generate_password_hash


cert = certifi.where()
dburi = config("DBURI")
client = motor.motor_asyncio.AsyncIOMotorClient(dburi, tlsCAFile=cert)
database = client.SupportDesk
userCollection = database.users
ticketCollection = database.tickets

async def dbRegisterUser(user : dict):
    existingUserCheck = await userCollection.find_one({"email": user["email"]})
    if existingUserCheck != None:
        raise HTTPException(status_code=400, detail="User already exist")
    password = generate_password_hash(user["password"])
    user["password"] = password
    newUser = await userCollection.insert_one(user)
    insertedID = str(newUser.inserted_id)
    user["id"] = insertedID
    accessToken = signJWT(insertedID)
    user["token"] = accessToken
    user.pop("_id")
    user.pop("password")
    return user

import motor.motor_asyncio
import certifi
from fastapi import HTTPException


cert = certifi.where()
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017', tlsCAFile=cert)
database = client.SupportDesk
userCollection = database.users
ticketCollection = database.tickets

async def dbRegisterUser(user : dict):
    print(user["email"])
    existingUserCheck = await userCollection.find_one({"email": user["email"]})
    if existingUserCheck != None:
        raise HTTPException(status_code=400, detail="User already exist")
    insertedID = str(userCollection.insert_one(user).inserted_id)
    return {"new" : insertedID}

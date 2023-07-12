import motor.motor_asyncio
import certifi
from fastapi import HTTPException
from decouple import config
from .auth.jwtHandler import signJWT, decodeJWT
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId


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

async def dbLoginUser(login : dict):
    existingUser = await userCollection.find_one({"email" : login["email"]})
    if existingUser != None and check_password_hash(existingUser["password"], login["password"]):
        existingUser.pop("password")
        userID = str(existingUser["_id"])
        existingUser.pop("_id")
        existingUser.pop("isAdmin")
        existingUser["id"] = userID
        accessToken = signJWT(userID)
        existingUser["token"] = accessToken
        return existingUser
    raise HTTPException(status_code=400, detail="Invalid Credentials")

async def dbUserInfo(token : str):
    access_token = decodeJWT(token)
    _id = ObjectId(access_token["userID"])
    user = await userCollection.find_one({"_id" : _id})
    user.pop("_id")
    user.pop("password")
    user.pop("isAdmin")
    user["id"] = access_token["userID"]
    return user


# TICKET FUNCTIONS

async def dbGetAllTickets(token : str):
    access_token = decodeJWT(token)
    userID = ObjectId(access_token["userID"])
    tickets = ticketCollection.find({"user":userID})
    ticketList = []
    for ticket in await tickets.to_list(length=20):
        print("test")
        ticket["_id"] = str(ticket["_id"])
        ticket["user"] = str(ticket["user"])
        ticketList.append(ticket)
    return ticketList
    

async def dbCreateTicket(ticket : dict, token : str):
    access_token = decodeJWT(token)
    userID = ObjectId(access_token["userID"])
    ticket['user'] = userID
    new_ticket = await ticketCollection.insert_one(ticket)
    ticket['_id'] = str(ticket["_id"])
    ticket['user'] = str(ticket['user'])
    return ticket

async def dbGetTicket(ticketID : str, token : str):
    access_token = decodeJWT(token)
    userID = ObjectId(access_token["userID"])
    try:
        ticketID = ObjectId(ticketID)
        ticket = await ticketCollection.find_one({"_id" : ticketID})
        if ticket["user"] == userID:
            ticket["_id"] = str(ticket["_id"])
            ticket["user"] = str(ticket["user"])
            return ticket
    except:
        raise HTTPException(status_code=400, detail="Invlaid Ticket ID")
    raise HTTPException(status_code=403, detail="Unauthorized Access")

async def dbDeleteTicket(ticketID : str, token : str):
    access_token = decodeJWT(token)
    userID = ObjectId(access_token["userID"])
    try:
        ticketID = ObjectId(ticketID)
        ticket = await ticketCollection.find_one({"_id" : ticketID})
        if ticket["user"] == userID:
            result = await ticketCollection.delete_one({"_id" : ticketID})
            return {"detail" : "Ticket has been deleted"}
    except:
        raise HTTPException(status_code=400, detail="Invlaid Ticket ID")
    raise HTTPException(status_code=403, detail="Unauthorized Access")

async def dbUpdateTicket(ticketID, ticket : dict, token : str):
    access_token = decodeJWT(token)
    userID = ObjectId(access_token["userID"])
    try: 
        ticketID = ObjectId(ticketID)
        dbTicket = await ticketCollection.find_one({"_id" : ticketID})
        if dbTicket["user"] == userID:
            updates = {}
            for x,y in ticket.items():
                if y != None:
                    updates[x] = y
            updatedTicket = await ticketCollection.update_one({"_id" : ticketID}, {"$set": updates})
            dbTicket = await ticketCollection.find_one({"_id" : ticketID})
            dbTicket["_id"] = str(dbTicket["_id"])
            dbTicket["user"] = str(dbTicket["user"])
            return dbTicket
    except:
        raise HTTPException(status_code=400, detail="Invlaid Ticket ID")
    raise HTTPException(status_code=403, detail="Unauthorized Access")    
    
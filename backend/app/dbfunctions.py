import motor.motor_asyncio
from model import UserSchema


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.SupportDesk
userCollection = database.users
ticketCollection = database.tickets
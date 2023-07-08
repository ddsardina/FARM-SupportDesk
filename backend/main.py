from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from app.model import UserSchema, UserLoginSchema
from app.dbfunctions import dbRegisterUser, dbLoginUser


app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Test Get Post to Verify API is up
@app.get("/", tags=["test"])
def test():
    return {"Hello" : "World"}

# USER ROUTES

# Register User
@app.post("/api/users", status_code=201, tags=["user"])
async def registerUser(user : UserSchema):
    userJSON = jsonable_encoder(user)
    response = await dbRegisterUser(userJSON)
    return response

# Login User
@app.post("/api/users/login", status_code=201, tags=["user"])
async def loginUser(login : UserLoginSchema):
    loginJSON = jsonable_encoder(login)
    response = await dbLoginUser(loginJSON)
    return response

# Get User Info
@app.get("api/users/me", tags=["user"])
def getMe():
    return {"Data" : "Get Me"}

# TICKET ROUTES

# Get All Tickets
@app.get("/api/tickets", tags=["tickets"])
def getAllTickets():
    return {"Data" : "Get All Tickets"}

# Create a New Ticket
@app.post("/api/tickets", tags=["tickets"])
def createTicket():
    return {"Data" : "Create Ticket"}

# Get Ticket By ID
@app.get("/api/ticket/{id}", tags=["tickets"])
def getTicketByID():
    return {"Data" : "Get Ticket by ID"}

# Delete Ticket By ID
@app.delete("/api/ticket/{id}", tags=["tickets"])
def deleteTicketByID():
    return {"Data" : "Delete Ticket by ID"}

# Update Ticket By ID
@app.put("/api/ticket/{id}", tags=["tickets"])
def updateTicketByID():
    return {"Data" : "Update Ticket by ID"}
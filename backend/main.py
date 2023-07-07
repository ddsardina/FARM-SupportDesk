from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
@app.post("/", tags=["user"])
def registerUser():
    return {"Data" : "Register User"}

@app.post("/login", tags=["user"])
def loginUser():
    return {"Data" : "Login User"}

@app.get("/me", tags=["user"])
def getMe():
    return {"Data" : "Get Me"}

# TICKET ROUTES

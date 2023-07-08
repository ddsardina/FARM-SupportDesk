from pydantic import BaseModel, Field, EmailStr

#Come back to Enum Product and Status

class UserSchema(BaseModel):
    name : str
    email : EmailStr
    password : str
    isAdmin : bool = Field(default=False)
    class Config:
        schema_extra = {
            "user_demo" : {
                "name" : "Daniel",
                "email" : "test@gmail.com",
                "password" : "Pass123word"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr
    password : str
    class Config:
        schema_extra = {
            "login_demo" : {
                "email" : "test@gmail.com",
                "password" : "Pass123word"
            }
        }

class TicketSchema(BaseModel):
    user : str = Field(default=None)
    product : str = Field(default=None)
    description : str = Field(default=None)
    status : str = Field(default="new")
    #come back for timestamp
    timestamp : str = Field(default=None)
    class Config:
        schema_extra = {
            "ticket_demo" : {
                "user" : "63203ea449c80078177497a6",
                "product" : "Laptop",
                "description" : "Screen is broken",
                "status" : "new",
                "timestamp" : "20220911T213835.000Z"
            }
        }
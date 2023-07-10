from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwtHandler import decodeJWT

class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error : bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request : Request):
        credentials : HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, details="Invalid authentication scheme")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired Token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, details="Invalid or Expired Token!")
        
    def verify_jwt(self, jwttoken : str):
        isTokenValid : bool = False
        try:
            payload = decodeJWT(jwttoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
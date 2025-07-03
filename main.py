from fastapi import FastAPI,HTTPException,status,Depends
from fastapi.security import  HTTPBasic,HTTPBasicCredentials
from starlette.middleware.cors import CORSMiddleware
# import  mysql.connector
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

security=HTTPBasic()
VALID_USERNAME="VEBBOX"
VALIV_PASSWORD="12345"
@app.get("/")
def basic_auth(credentials:HTTPBasicCredentials= Depends(security)):
    if credentials.username != VALID_USERNAME or credentials.password != VALIV_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate":"basic"},
        )
    return credentials.username

from fastapi import FastAPI
import logging

from db.databaseConfig import init_db

import users 
from users import usersRouters 
from users.models.userModel import User
app = FastAPI()

logging.basicConfig(filename='app.log',
                    # filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', 
                    )

log = logging.getLogger("uvicorn")

app.include_router(usersRouters.router)

@app.get("/")
async def root():    
    try:
        message = {"Hello": "World!"}
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    return message


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    await init_db()


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")    
    

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0", port=80, reload=True)
from fastapi import FastAPI
import logging
from db.init_database import init_database

from db.databaseConfig import init_db
from comunication.rabbit_init  import publish
# from celerys.celeryWorker import create_order

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
    log.info("INIT: ___Starting up___")
    await init_db()
    # await init_database()
    log.info("INIT: ___end___")
    
# Create order endpoint
@app.post('/order')
def add_order():
#     # use delay() method to call the celery task
    publish()
    return {"message": "Order Received! Thank you for your patience."}


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")    
    

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0", port=80, reload=True)
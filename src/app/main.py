from fastapi import FastAPI
import logging
# from db.init_database import init_database

from db.databaseConfig import init_db
# from comunication.rabbit_init  import publish
from workers.tasks import create_order, init_consume

from celery.result import AsyncResult

import users 
from users import userRouters 
from users import userLogin
from users.models.userModel import UserDB

from items.routers import itemRouters
from items.models.itemModel import ItemDB

from docs.export_docs import markdown_exporter


app = FastAPI(
    title="User Backend", 
    description=markdown_exporter.export_md_files_as_text()
)

logging.basicConfig(filename='app.log',
                    # filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', 
                    )

log = logging.getLogger("uvicorn")

app.include_router(userLogin.router)
app.include_router(userRouters.router)
app.include_router(itemRouters.router)

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
    init_consume.delay()
    # await init_database()
    log.info("INIT: ___end___")
    
# Create order endpoint
@app.post('/order')
async def add_order():
#     # use delay() method to call the celery task
    task = create_order.delay("name", 5)
    # publish()
    return {"message": "Order Received! Thank you for your patience.",
            "task id": task.id}

@app.post('/order2')
async def add_order2(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result
    return  {"message":  task_result.ready()}


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")    
    

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0", port=80, reload=True)
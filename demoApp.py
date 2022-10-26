from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from database import Base, engine,User
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(engine)

class UserApiModel(BaseModel):
    name: str
    lastname: str

    class Config:
        orm_mode = True

@app.get("/")
async def root():
    return {"status": "Ok"}

@app.post("/kayit")
async def register(item: UserApiModel):
    try:
        session = Session(bind=engine, expire_on_commit=False)

        data= User(
            name=item.name,
            lastname=item.lastname
            )
        
        session.add(data)
        session.commit()
        session.close()
        return {"result": "Ok"}
    except:
        return {"result": "Error"}


@app.get("/list")
async def getList():
    try:
        session = Session(bind=engine, expire_on_commit=False)
        data = session.query(User).all()
        return {"result": data}
    except:
        return {"result": "Error"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
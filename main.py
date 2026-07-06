from fastapi import FastAPI


from db import SessionLocal 
from schema import User
from model import User as UserModel 
import model
from db import engine

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

@app.post("/users/")
def create_user(user: User):
    db = SessionLocal()
    db_user = UserModel(id=user.id, email=user.email, name=user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

from typing import List

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, select

from db import create_db_and_tables, get_session
from model import TestUser, TestUserCreate, TestUserGet, TestUserUpdate

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# 　ユーザー情報一覧取得
@app.get("/test_users/", response_model=List[TestUserGet])
def get_users(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    users = session.exec(select(TestUser).offset(offset).limit(limit)).all()
    return users


# ユーザー情報取得(id指定)
@app.get("/test_users/{user_id}", response_model=TestUserGet)
def get_user(*, session: Session = Depends(get_session), user_id: int):
    user = session.get(TestUser, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ユーザ情報登録
@app.post("/test_users/", response_model=TestUserGet)
def post_user(*, session: Session = Depends(get_session), user: TestUserCreate):
    db_user = TestUser.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


# ユーザ情報更新
@app.patch("/test_users/{user_id}", response_model=TestUserGet)
def update_users(*, session: Session = Depends(get_session), user_id: int, user: TestUserUpdate):
    db_user = session.get(TestUser, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

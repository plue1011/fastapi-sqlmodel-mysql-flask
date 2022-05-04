from typing import Optional

from sqlmodel import Field, SQLModel


class TestUserBase(SQLModel):
    name: str = Field(index=True)
    email: str = Field(index=True)


class TestUser(TestUserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TestUserCreate(TestUserBase):
    pass


class TestUserGet(TestUserBase):
    id: int


class TestUserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None

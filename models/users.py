from pydantic import BaseModel, Field, RootModel

from utils.generate_fake_data import random_name, random_email, random_gender, random_status


class DefaultUser(BaseModel):
    id: int
    name: str
    email: str
    gender: str
    status: str


class CreateUser(BaseModel):
    name: str = Field(default_factory=random_name)
    email: str = Field(default_factory=random_email)
    gender: str = Field(default_factory=random_gender)
    status: str = Field(default_factory=random_status)


class UpdateUser(BaseModel):
    name: str | None = Field(default_factory=random_name)
    email: str | None = Field(default_factory=random_email)
    gender: str | None = Field(default_factory=random_gender)
    status: str | None = Field(default_factory=random_status)


class DefaultUsersList(RootModel):
    root: list[DefaultUser]

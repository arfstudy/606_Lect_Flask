from typing import Optional

from pydantic import BaseModel, field_validator, validator


class CreateUser(BaseModel):
    name: str
    password: str

    @field_validator("password")
    def secure_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password is not to short")
        return value


class UpdateUser(BaseModel):
    name: Optional[str]
    password: Optional[str]

    @field_validator("password")
    def secure_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password is to short")
        return value

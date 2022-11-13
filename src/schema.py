from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class SignUp(BaseModel):
    email: str
    password: str
    confirm_password: str
    username: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class SignUpResponse(BaseModel):
    email: str
    email_verified: bool
    password: str
    confirm_password: str
    username: str
    first_name: str
    last_name: str


class Users(BaseModel):
    details: List


class LogIn(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    token: str


class Event(BaseModel):
    title: str
    description: str
    scheduled_at: str
    location: str
    expected_no_of_attendees: int


class EventResponse(BaseModel):
    event_id: int
    user: str
    description: str
    expected_no_of_attendees: int
    created_at: str
    updated_at: str
    scheduled_at: str
    location: str
    active: bool


class RequestEvent(BaseModel):
    event_id: int


class RequestEventResponse(BaseModel):
    title: str
    description: str
    expected_no_of_attendees: int
    location: str
    scheduled_at: str


class UpdateEvent(BaseModel):
    title: str
    description: str
    expected_no_of_attendees: int
    location: str
    scheduled_at: str


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class Poll(BaseModel):
    name: str
    email: str
    poll_option: int


class UserDetails(BaseModel):
    email: str
    first_name: str
    last_name: str
    current_password: str
    profile_photo: str

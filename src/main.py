from fastapi import FastAPI
import schema

app = FastAPI()


@app.post("/signup", response_model=schema.SignUpResponse)
async def sign_up(data: schema.SignUp):
    pass


@app.post("/login", response_model=schema.LoginResponse)
async def login(data: schema.LogIn):
    pass


@app.post("/logout")
async def logout():
    pass


@app.post("/forget_password")
async def forget_password():
    pass


@app.get("/users", response_model=list[schema.UserDetails])
async def get_users():
    pass


@app.post("/event", response_model=schema.EventResponse)
async def create_event(data: schema.Event):
    pass


@app.get("/user/events/{event_id}", response_model=schema.RequestEventResponse)
async def get_event(event_id: int):
    pass


@app.put("/user/events/{event_id}")
async def update_event(event_id: int, data: schema.UpdateEvent):
    pass


@app.delete("/user/events/{event_id}")
async def delete_event(event_id: int):
    pass


@app.get("/event/{event_id}/poll")
async def get_poll(event_id: int, data: schema.Poll):
    pass


@app.get("/user_details", response_model=schema.UserDetails)
async def get_user_details():
    pass

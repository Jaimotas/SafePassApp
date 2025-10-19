from fastapi import FastAPI
from routers import users, auth

app = FastAPI(title="SafePass API")

app.include_router(users.router)
app.include_router(auth.router)

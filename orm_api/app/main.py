from fastapi import FastAPI
import uvicorn

from app.urls import bestiaries, users, compatibilities, pairings, triangles


app = FastAPI()
app.include_router(users.router, prefix='/api/v1')


def main():
    uvicorn.run(app, host='0.0.0.0', port=5000, log_level='info')


if __name__ == "__main__":
    main()

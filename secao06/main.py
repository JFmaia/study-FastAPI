from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso Api - Segurança')

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)


"""
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzA5MDM4MjU1LCJpYXQiOjE3MDg0MzM0NTUsInN1YiI6IjYifQ.1_OmQMAS20lLt6qAaKaJJ2v7F6Sx7j75FrH-hk_1hwI
tipo:bearer
"""
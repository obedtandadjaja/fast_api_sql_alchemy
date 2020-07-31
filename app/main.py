import time
from typing import Optional

from fastapi import FastAPI, Header, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.api import root


WHITELISTED_ROUTES = [
    '/api/health',
    '/api/v1/login',
]

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # TODO(obedt): remove this once the project is live
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Authentication middleware
@app.middleware("http")
async def verify_authentication_token(request: Request, call_next):
    # If path is in whitelisted routes then skip this middleware
    if request.url.path in WHITELISTED_ROUTES:
        return await call_next(request)

    try:
        authentication_token = request.headers['authorization']
        if authentication_token.startswith('Bearer'):
            authentication_token = authentication_token[6:]

        if authentication_token == 'secret':
            return await call_next(request)
        else:
            return Response(content='Invalid credentials', status_code=401)
    except KeyError:
        return Response(content='Invalid credentials', status_code=401)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(root.router, prefix='/api', tags=['api'])

"""Summary here.

Details here.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post('/login')
async def login(email: str, password: str):
    # TODO(obedt): change implementation and change this hard coded logic
    if email == 'obed.tandadjaja@gmail.com' and password == 'password':
        return {'status': 'OK'}
    else:
        raise HTTPException(status_code=400, detail='Invalid credentials')

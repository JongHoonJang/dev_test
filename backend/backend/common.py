import jwt
from rest_framework.response import Response
from .settings import SIMPLE_JWT
from rest_framework import status

def checkuser(token):
    if token is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED) 
    # header에서 받은 token 내용에 선행값 (ex. Bearer)이 있다면 token값이랑 분리 시켜준다.
    # 'bearer 토큰값'
    type, jwt_token = token.split(' ')
    user_token = jwt.decode(
    jwt_token,
    SIMPLE_JWT.get('SIGNING_KEY'),
    algorithms=[SIMPLE_JWT.get('ALGORITHM')],
    )
    return user_token.get('user_id')
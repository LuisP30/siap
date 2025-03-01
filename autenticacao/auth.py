from ninja.security import HttpBearer
import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError, InvalidTokenError
from django.conf import settings
from datetime import timezone, timedelta, datetime

SECRET_KEY = settings.SECRET_KEY
ALGORITMO = 'HS256'

def gera_token(usuario):
    payload_access = {
            "id_user": usuario['id'],
            "nome": usuario['nome'],
            "sobrenome": usuario['sobrenome'],
            "permissao": usuario['permissao'],
            "type": "access",
            "iat": int(datetime.now(timezone.utc).timestamp()),
            "exp": int((datetime.now(timezone.utc) + timedelta(minutes=30)).timestamp())
        }
    payload_refresh = {
        "id_user": usuario['id'],
        "nome": usuario['nome'],
        "sobrenome": usuario['sobrenome'],
        "permissao": usuario['permissao'],
        "type": "refresh",
        "iat": int(datetime.now(timezone.utc).timestamp()),
        "exp": int((datetime.now(timezone.utc) + timedelta(hours=6)).timestamp())
    }
    access_token = jwt.encode(payload=payload_access, key=settings.SECRET_KEY)
    refresh_token = jwt.encode(payload=payload_refresh, key=settings.SECRET_KEY)
    return {"access_token": access_token, "refresh_token": refresh_token}

def decodifica_token(token: str, tipo_esperado: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        if payload['type'] == tipo_esperado:
            return payload
        else:
            raise InvalidTokenError(f"Token de tipo errado. Envie um token de tipo '{tipo_esperado}'")
    except DecodeError as e:
        raise InvalidTokenError("Token inválido.") from e
    except ExpiredSignatureError as e:
        raise InvalidTokenError("O token expirou. Por favor, faça login novamente.") from e
    except InvalidTokenError as e:
        raise InvalidTokenError(str(e))
    
class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        payload = decodifica_token(token, 'access')
        if payload is None:
            print('Tipo de token errado')
            return None
        return payload
from ninja import Router
from ..auth import gera_token, decodifica_token
from django.contrib.auth import authenticate
from django.http import JsonResponse
from ninja.responses import Response
from .schemas import AnuncianteCadastroSchema, AnuncianteLoginSchema, TokensJWTSchema, RefreshTokenSchema
from autenticacao.models import Anunciante

autenticacao_router = Router()

# ENDPOINT PARA LOGIN
@autenticacao_router.post('/login', response=TokensJWTSchema, tags=['Controle de acesso e autenticação'])
def login(request, usuario: AnuncianteLoginSchema):
    usuario_logado = authenticate(request, username=usuario.email, password=usuario.password)
    if usuario_logado:
        usuario_dict = {
            "id": usuario_logado.id,
            "username": usuario_logado.username,
            "cnpj": usuario_logado.cnpj,
            "email": usuario_logado.email
        }
        tokens = gera_token(usuario_dict)
        return JsonResponse({"access_token": tokens["access_token"], "refresh_token": tokens["refresh_token"]}, status=200)
    return JsonResponse({"Erro": "Login ou senha inválidos"}, status=401)

# ENDPOINT PARA CADASTRO
@autenticacao_router.post('/cadastro', response=AnuncianteCadastroSchema, tags=['Controle de acesso e autenticação'])
def cadastro(request, usuario: AnuncianteCadastroSchema):
    
    if Anunciante.objects.filter(username=usuario.username).exists():
        return JsonResponse({"Erro": "Este nome de empreendimento já está em uso"}, status=409)
    if Anunciante.objects.filter(cnpj=usuario.cnpj).exists():
        return JsonResponse({"Erro": "Este CNPJ já está em uso"}, status=409)
    if Anunciante.objects.filter(email=usuario.email).exists():
        return JsonResponse({"Erro": "Este e-mail já está em uso"}, status=409)

    anunciante = Anunciante.objects.create_user(
        username=usuario.username, 
        email=usuario.email, 
        cnpj=usuario.cnpj,
        endereco=usuario.endereco,
        telefone=usuario.telefone,
        whatsapp=usuario.whatsapp,
        instagram=usuario.instagram
    )
    return anunciante

# ENDPOINT PARA RENOVAÇÃO DE TOKENS
@autenticacao_router.post('/renova_tokens', response=TokensJWTSchema, tags=['Controle de acesso e autenticação'])
def renova_tokens(request, RefreshToken: RefreshTokenSchema):
    payload = decodifica_token(RefreshToken.refresh_token, 'refresh')
    usuario = {
        "id": payload.id,
        "username": payload.username,
        "cnpj": payload.cnpj,
        "email": payload.email
    }
    tokens = gera_token(usuario)
    return tokens

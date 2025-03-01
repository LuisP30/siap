from ninja import NinjaAPI
from autenticacao.api.router import autenticacao_router
from anuncios.api.router import anuncios_router

api = NinjaAPI()

api.add_router('/auth', autenticacao_router)
api.add_router('/anuncios', anuncios_router)
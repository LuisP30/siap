from ninja import ModelSchema, Schema
from autenticacao.models import Anunciante

class AnuncianteCadastroSchema(ModelSchema):
    class Config(Schema.Config):
        model = Anunciante
        model_fields = ['username', 'email', 'cnpj', 'endereco', 'telefone', 'whatsapp', 'instagram', 'password']
        
class AnuncianteLoginSchema(ModelSchema):
    class Config(Schema.Config):
        model = Anunciante
        model_fields = ['email', 'password']

class TokensJWTSchema(Schema):
    access_token: str
    refresh_token: str

class RefreshTokenSchema(Schema):
    refresh_token: str
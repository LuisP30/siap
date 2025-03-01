from ninja import Schema, Form, ModelSchema
from ..models import Anuncio
from typing import Optional
from datetime import date

class AnuncioCreateSchema(Schema):
    titulo: str = Form(...)
    descricao: str = Form(...)
    preco_anterior: float = Form(...)
    preco_atual: float = Form(...)
    validade: date = Form(...)
    seguimento: int = Form(...)

class AnuncioResponseSchema(ModelSchema):
    class Config(Schema.Config):
        model = Anuncio
        model_fields = '__all__'

class AnuncioPatchSchema(Schema):
    titulo: Optional[str] = Form(None)
    descricao: Optional[str] = Form(None)
    preco_anterior: Optional[float] = Form(None)
    preco_atual: Optional[float] = Form(None)
    validade: Optional[date] = Form(None)
    seguimento: Optional[int] = Form(None)
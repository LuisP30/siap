from ninja import Router, File, Form
from ninja.files import UploadedFile
from ninja.responses import Response
from autenticacao.auth import AuthBearer
from autenticacao.models import Anunciante
from .schemas import AnuncioCreateSchema, AnuncioResponseSchema, AnuncioPatchSchema, SeguimentoSchema, SeguimentoPostSchema
from anuncios.models import Anuncio, Seguimento
from django.http import JsonResponse
from typing import List, Optional
from django.db.models import Q

anuncios_router = Router(auth=AuthBearer())

# ENDPOINTS PARA CRUD DE ANÚNCIOS
@anuncios_router.get('/', response=List[AnuncioResponseSchema], tags=['Anúncios'], auth=None)
def lista_anuncios(request, query: Optional[str] = None):
    if query:
        anuncios = Anuncio.objects.filter(
            Q(titulo__icontains=query) | Q(anunciante__username__icontains=query)
        )
        return anuncios

    anuncios = Anuncio.objects.all()
    return anuncios

@anuncios_router.post('/', response=AnuncioCreateSchema, tags=['Anúncios'])
def cria_anuncio(request, titulo: str = Form(...), descricao: str = Form(...), preco_anterior: float = Form(...),
                  preco_atual: float = Form(...), validade: str = Form(...), seguimento: int = Form(...),
                  foto: UploadedFile = File(...), anunciante_id: int = Form(...)):
    print(anunciante_id)
    seguimento_obj = Seguimento.objects.get(id=seguimento)  # Tratar erro caso não encontre
    anunciante = Anunciante.objects.get(id=anunciante_id)

    # Criar o anuncio
    anuncio = Anuncio.objects.create(
        titulo=titulo,
        descricao=descricao,
        preco_anterior=preco_anterior,
        preco_atual=preco_atual,
        validade=validade,
        seguimento=seguimento_obj,
        anunciante=anunciante
    )

    # Salvar a foto no campo de foto
    anuncio.foto.save(foto.name, foto)
    anuncio.save()

    return Response({
        "id": anuncio.id,
        "titulo": anuncio.titulo,
        "descricao": anuncio.descricao,
        "preco_anterior": anuncio.preco_anterior,
        "preco_atual": anuncio.preco_atual,
        "validade": anuncio.validade,
        "seguimento": anuncio.seguimento.id,  # Aqui, apenas o ID do Seguimento
    }, status=201)

@anuncios_router.delete('/{int:id_anuncio}', tags=['Anúncios'])
def remove_anuncio(request, id_anuncio: int):
    anuncio = Anuncio.objects.get(id=id_anuncio)
    anuncio.delete()
    return JsonResponse({"messagem":"Anúncio removido com sucesso!"}, status=200)

@anuncios_router.patch('/{int:id_anuncio}', response=AnuncioResponseSchema, tags=['Anúncios'])
def edita_anuncio(request, id_anuncio: int, dados: AnuncioPatchSchema = Form(...), foto: Optional[UploadedFile] = File(None)):
    anuncio = Anuncio.objects.get(id=id_anuncio)
    campos_atualizados = dados.dict(exclude_unset=True)
    
    # Editando campos:
    # Alterando foto e seguimento separadamente
    if 'seguimento' in dados:
        seguimento_id = dados.pop('seguimento')
        anuncio.seguimento_id = seguimento_id
    if foto:
        anuncio.foto.save(foto.name, foto)
    
    for chave, valor in campos_atualizados.items():
        setattr(anuncio, chave, valor)

    anuncio.save()
    return anuncio

@anuncios_router.post('/seguimento', response=SeguimentoSchema, tags=['Seguimento'])
def cria_seguimento(request, seguimento: SeguimentoPostSchema):
    seguimento = Seguimento.objects.create(nome=seguimento.nome)
    return seguimento

@anuncios_router.get('/seguimento', response=List[SeguimentoSchema], tags=['Seguimento'])
def consulta_seguimentos(request):
    seguimentos = Seguimento.objects.all()
    return seguimentos
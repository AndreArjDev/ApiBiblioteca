from django.db import models
from uuid import uuid4

# Create your models here.

def uploadCapalivro(instance, filename):
    return f'{instance.id_livro} - {filename}'

class livro(models.Model):
    id_livro = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_da_edicao = models.IntegerField()
    estado = models.CharField(max_length=50)
    pags = models.IntegerField()
    editora = models.CharField(max_length=255)
    isercao_no_cadastro = models.DateField(auto_now_add=True)
    capa_livro = models.ImageField(upload_to=uploadCapalivro, blank=True, null=True)

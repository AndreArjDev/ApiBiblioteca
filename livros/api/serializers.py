from rest_framework import serializers
from livros import models

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.livro
        fields = '__all__'

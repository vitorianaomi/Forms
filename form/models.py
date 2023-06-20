from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length = 150)
    email = models.EmailField()
    data_nascimento = models.DateField()

class Professor(models.Model):
    nome = models.CharField(max_length = 150)
    matricula = models.CharField(max_length = 14)
    email = models.EmailField()
    disciplina = models.CharField(max_length = 100)

class Projeto(models.Model):
    nome = models.CharField(max_length = 150)
    descricao = models.TextField()
    data_criacao = models.DateField()

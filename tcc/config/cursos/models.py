from django.db import models


class Materia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    nivel = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    
class Aula(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="aulas") #(on_delete=models.CASCADE) signiica que caso uma matéria for apagada, todas as aulas vinculadas, serão apagadas também
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return f"{self.materia.nome} - {self.titulo}"
    
    
    
class Exercicio(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name="exercicios")
    enunciado = models.TextField()
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    resposta = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    
    def __str__(self):
        return f"{self.aula.titulo} - {self.enunciado[:30]}..."

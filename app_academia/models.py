from django.db import models

class Cadastrar(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Senha: {self.senha}'
    def set_password(self, raw_password):
        from django.contrib.auth.hashers import make_password
        self.senha = make_password(raw_password)
    
    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.senha)

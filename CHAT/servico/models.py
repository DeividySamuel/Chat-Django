from django.db import models

class Servico(models.Model):
    choices_sexo = (('F', 'Feminino'),
                    ('M', 'Masculino'))
   
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=19)
    cpf = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    email = models.EmailField()
    modelo = models.CharField(max_length=100)
    detalhes = models.CharField(max_length=100)
    relato_do_cliente = models.TextField()
    servico_a_ser_prestado = models.CharField(max_length=255)
    observacao = models.CharField(max_length=255)
    valor_dos_servico = models.IntegerField()
    valor_das_pecas = models.IntegerField()
    valor_total = models.IntegerField()

    
    def __str__(self):
        return self.nome




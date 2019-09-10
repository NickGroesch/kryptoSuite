from django.db import models


class Alphabet(models.Model):
    name = models.CharField(max_length=50)
    alphabet_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class CipherText(models.Model):
    name = models.CharField(max_length=50)
    ciphertext = models.CharField(max_length=10000)
    alpahabet = models.ForeignKey(Alphabet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=50)
    keyword = models.CharField(max_length=100)
    alpahabet = models.ForeignKey(Alphabet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.

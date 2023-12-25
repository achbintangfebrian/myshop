from django.db import models
from django.contrib import admin

# Create your models here.

class Kategori(models.Model):
    namaProduk = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.namaProduk}"


class Produk(models.Model):        
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()

    def __str__(self):
        return f"{self.nama}"
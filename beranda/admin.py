from django.contrib import admin
from .models import Produk, Kategori

# Register your models here.
class ProdukKategori(admin.ModelAdmin):
    list_display = (
        "nama",
        "harga",
    )

admin.site.register(Produk, ProdukKategori)
admin.site.register(Kategori)

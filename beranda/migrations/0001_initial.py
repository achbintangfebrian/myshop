# Generated by Django 4.2.7 on 2023-11-10 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaProduk', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('harga', models.IntegerField()),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beranda.kategori')),
            ],
        ),
    ]

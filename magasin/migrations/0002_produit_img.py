# Generated by Django 5.0.2 on 2024-02-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='Img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_professor_matricula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateField()),
            ],
        ),
    ]

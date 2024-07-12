# Generated by Django 5.0.6 on 2024-05-26 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('subtotal', models.PositiveIntegerField()),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.boleta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2024-03-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vistaprevia", "0006_alter_categoria_id_alter_producto_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="descripcion",
            field=models.TextField(blank=True, null=True),
        ),
    ]

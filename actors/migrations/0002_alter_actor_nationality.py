# Generated by Django 5.0.6 on 2024-06-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil'), ('CANADA', 'Canada')], max_length=100, null=True),
        ),
    ]

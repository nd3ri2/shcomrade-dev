# Generated by Django 4.1.7 on 2023-03-23 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_investment_amount_invested_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='principal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.transaction'),
        ),
        migrations.AlterField(
            model_name='member',
            name='registration',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.registration'),
        ),
    ]

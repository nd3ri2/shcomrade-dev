# Generated by Django 4.1.7 on 2023-03-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_investment_principal_alter_member_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='joined_on',
            field=models.DateField(auto_now=True),
        ),
    ]

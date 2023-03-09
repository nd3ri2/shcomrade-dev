# Generated by Django 4.1.7 on 2023-03-09 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_investment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_number', models.CharField(max_length=8)),
                ('member_password', models.CharField(max_length=8)),
                ('joined_on', models.DateField(auto_now_add=True)),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.registration')),
            ],
        ),
    ]

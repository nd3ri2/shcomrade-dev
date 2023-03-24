from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.db.models import F, Q

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name


class Member(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.PROTECT)
    member_number = models.CharField(max_length=8)
    member_password = models.CharField(max_length=8)
    joined_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.member_number
    
    def del_obj(self):
        obj = Registration.objects.get(id=self.registration_id)
        obj.delete()


class Transaction(models.Model):
    types = (
        ('CTB', 'Contribution'),
        ('RPT', 'Repayment'),
        ('INV', 'Investment')
    )

    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=3, choices=types)
    amount = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.transaction_type} on {self.date}'


class Investment(models.Model):
    principal = models.OneToOneField(Transaction, on_delete=models.PROTECT)
    investment_name = models.CharField(max_length=20)
    investment_rate = models.FloatField()

    def __str__(self):
        return self.investment_name
    
    

class Leaver(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    notice_given = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.member} notice given on {self.notice_given}'

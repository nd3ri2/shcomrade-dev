from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name


class Member(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.PROTECT)
    member_number = models.CharField(max_length=8)
    member_password = models.CharField(max_length=8)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.member_number



class Investment(models.Model):
    investment_name = models.CharField(max_length=20)
    amount_invested = models.PositiveIntegerField()
    invested_on = models.DateField(auto_now=True)
    investment_rate = models.FloatField()

    def __str__(self):
        return self.investment_name

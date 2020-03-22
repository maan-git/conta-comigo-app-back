import datetime
from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country}, {self.zip_code}, {self.address}, {self.province}, {self.city}"


class Person(models.Model):
    gender_choices = [('Male', 'Male'),
                      ('Female', 'Female')]
    live_alone_choices = [('Yes', 'Yes'),
                          ('No', 'No')]
    risk_group_choices = [('Yes', 'Yes'),
                          ('No', 'No')]
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=6, choices=gender_choices)
    birthday_date = models.DateField()
    ddi = models.CharField(max_length=4)
    phone = models.CharField(max_length=15)
    live_alone = models.CharField(max_length=3, choices=live_alone_choices)
    risk_group = models.CharField(max_length=3, choices=risk_group_choices)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE)
    complement = models.CharField(max_length=80, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.gender}, {datetime.date.today() - self.birthday_date}"


class Post(models.Model):
    post_type_choices = [('Help me', 'Help me'),
                         ('To help', 'To help')]

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    post_text = models.TextField()
    post_type = models.CharField(max_length=8, choices=post_type_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_helps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.post_type}, {self.post_type}"

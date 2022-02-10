from django.db import models


class Address(models.Model):
    account = models.CharField(max_length=42, null=False, blank=False)
    balance = models.IntegerField()

    def __str__(self):
        return f'{self.account} - {self.balance}'

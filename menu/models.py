from django.db import models


class Nation(models.Model):
    """
        Stores the nation of fooa, i.e: thai, eng etc.
    """
    nation = models.CharField(max_length=200)

    def __str__(self):
        return self.nation


class Foodlist(models.Model):
    foodname = models.CharField(max_length=200)
    nation = models.ForeignKey(Nation, on_delete=models.SET_NULL, null=True)


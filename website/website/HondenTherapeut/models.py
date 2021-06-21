from django.db import models


class Hond(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + ' (' + str(self.id) + ')'

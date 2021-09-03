from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    completed =  models.BooleanField(default=False, null=True, blank=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True,blank=True)


    class Meta:

        ordering = ['-date_created',]

    def __str__(self):
        return f' {self.name} {self.completed}'
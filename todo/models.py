from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField('Nomi',max_length=100)
    created_at = models.DateTimeField('Yaratilgan vaqti',auto_now_add=True)
    update_at = models.DateTimeField('Yangilangan vaqti',auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    # Para que en el admin se muestre el nombre del post
    # en lugar de mostrar Object(<id>)
    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    # Para que en el admin se muestre el nombre del post
    # en lugar de mostrar Object(<id>)
    def __str__(self):
        return self.title


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    # related_name se usa para acceder mas facil a los datos de a una relacion ManyToMany
    # Cuando quiera saber las Entrys que ha hecho un author solo digo author.entries.all()
    authors = models.ManyToManyField(Author, related_name='entries')
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

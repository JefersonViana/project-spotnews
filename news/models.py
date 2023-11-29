from django.db import models
from .validators import validate_sigle_title


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        validators=[validate_sigle_title],
    )
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=False, blank=True)
    categories = models.ManyToManyField(Category, blank=False)

    def __str__(self):
        return self.title

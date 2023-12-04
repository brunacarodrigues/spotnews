from django.db import models
from news.validations import title_validate


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
        null=False,
        blank=False,
        validators=[title_validate]
    )
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=False, null=False)

    def __str__(self):
        return self.title

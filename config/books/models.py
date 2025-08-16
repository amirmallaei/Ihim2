from ckeditor.fields import RichTextField
from django.db import models
from user.models import User
import uuid

# Create your models here.
class Book(models.Model):
    CATEGORY=(
        (0, "Science"),
        (1, "Historical"),
        (2, "True Crime"),
        (3, "Romance")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=150, help_text="The name of the book")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/books/', blank=True, null=True)
    category = models.PositiveIntegerField(choices=CATEGORY)
    abstract = RichTextField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    price = models.IntegerField(default = 10)
    count = models.PositiveIntegerField(default=0)
    pages = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.title
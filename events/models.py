from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Event(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Writer ")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
    event_image = models.FileField(blank = True,null = True,verbose_name="Add Photo to Event")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

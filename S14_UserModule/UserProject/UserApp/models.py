from django.db import models

# Create your models here.

class PostWork(models.Model):
    post_name = models.TextField(max_length=10)
    post_date = models.DateField(auto_created=True)
    post_disc = models.TextField(max_length=150)
    post_poster = models.FileField(upload_to="static/amanbhai_work")

    pass

class carousel:
    def __init__(self,title,disc,poster,link):
        self.title = title
        self.disc = disc
        self.poster = poster
        self.link = link
from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.author, self.date)
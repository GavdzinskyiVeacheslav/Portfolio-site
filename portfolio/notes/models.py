from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=150)
    full_text = models.TextField('Note', null=True)
    date = models.DateTimeField('Date of publication', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/notes/{self.id}'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

from django.db import models
from django.contrib.auth.models import User


class SeriesManager(models.Manager):
    
    def get_by_user(self, user):
        """ Returns all series related to a user """
        query_set = super().get_queryset().filter(user_id=user.id)
        return query_set
    
    def get_by_id(self, series_id):
        """ Gets series from id """
        series = super().get_queryset().get(id=series_id)
        return series
    
    def get_by_name(self, name):
        series = super().get_queryset().get(name=name)
        return series


class Series(models.Model):
    
    name = models.CharField(max_length=150)
    episode = models.IntegerField()
    season = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    
    objects = SeriesManager()

    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.name

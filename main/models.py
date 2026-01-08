from django.db import models


class Character(models.Model):
	name = models.CharField()
	alias = models.CharField()
	birthdate = models.DateField(null=True, blank=True)
	species = models.CharField()
	famous_phrase = models.CharField()
	citizenship = models.CharField()
	affiliatons = models.JSONField()
	portrayed_by = models.CharField()
	first_appearence = models.CharField()
	image1 = models.ImageField(upload_to='images/', default=None)
	image2 = models.ImageField(upload_to='images/', default=None)

	def __str__(self):
		return self.name
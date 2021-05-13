from django.db import models

class Publication(models.Model):
	nome = models.CharField(max_length=200)
	cwid = models.CharField(max_length=10)
	opicoes_bayflex = models.TextField()
	email = models.TextField()
	publication_date = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now_add=True)


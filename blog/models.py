from django.db import models

class Publication(models.Model):
	nome = models.CharFiels(max_length=200)
	cwid = models.CharField(max_length=10)
	opicoes_bayflex = models.TextFields()
	email = models.TextFields()
	publication_date = models.DateTimeFiels(auto_now_add=True)
	update_at = models.DateTimeFiels(auto_now_add=True)


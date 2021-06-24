from django.db import models

# Create your models here.
class dienchinhsach(models.Model):
	tendcs = models.CharField(max_length = 200)
	tilegiamhocphi = models.FloatField(default=0)
	def __str__(self):
		return self.tendcs
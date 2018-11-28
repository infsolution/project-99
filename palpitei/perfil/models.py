from django.db import models
from django.contrib.auth.models import User

class Lottery(models.Model):
	name = models.CharField(max_length=255)
	number_ten = models.IntegerField(default=0)
	def __str__(self):
		return self.name

class Contest(models.Model):
	number = models.IntegerField(default=0)
	lottery = models.ForeignKey(Lottery, on_delete = models.CASCADE, related_name='contests')
	date_contest = models.DateField(auto_now_add=False)
	def __str__(self):
		return str(self.number)
    
class Tips(models.Model):
	dt_tip = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='tipies')
	contest = models.ForeignKey(Lottery, on_delete = models.CASCADE, related_name='tipies')

class TenContest(models.Model):
	value = models.IntegerField(default=0)
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='ten_contests')
	def __str__(self):
		return str(self.value)


class TenTips(models.Model):
	value = models.IntegerField(default=0)
	tips = models.ForeignKey(Tips, on_delete=models.CASCADE, related_name='tipies')
	def __str__(self):
		return str(self.value)
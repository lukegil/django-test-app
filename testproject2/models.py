from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Questions(models.Model):
    question_text = models.TextField()
    updated_time = models.DateTimeField(auto_now = True, auto_now_add = True)

    def __unicode__(self):
        return self.question_text

class Answers(models.Model):
    answer_text = models.TextField()
    answer_ip = models.GenericIPAddressField()
    updated_time = models.DateTimeField(auto_now = True, auto_now_add = True)

    def __unicode__(self):
        return self.answer_text

    def get_todays_answers(self):
        return self.updated_time >= timezone.now() - datetime.timedelta(days=1)

        

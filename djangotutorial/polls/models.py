from django.db import models

# Create your models here.

"""
each model is represented by a class that subclasses 
django.db.models.Model. 
Each field is represented by an instance of a Field 
class – e.g., CharField for character fields and 
DateTimeField for datetimes. This tells Django what 
type of data each field holds.
"""

class Question(models.Model):
    # arguments: max_length is required for validation
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    # relationship defiined using foreign key
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # optional argument default sets the default value for the field
    votes = models.IntegerField(default=0)
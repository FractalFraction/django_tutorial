from django.db import models

# Create your models here.

# Models in Django subclass the the django.db.models.Model class
# Each model has class variables which represent the field in the database table
# Each class variable has the field date type specified by its value, an instance of a
# Field class 
class Stage(models.Model):
    # Fields 
    stage_number = models.IntegerField(default=1)
    stage_text = models.CharField(max_length=50)
    #Methods
    def __str__(self):
        return self.stage_text

class Question(models.Model):
    # Fields 
    stage = models.ForeignKey(Stage, db_column='stage_number', default=1, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    #Methods
    def __str__(self):
        return self.question_text
    
# Each choice belongs to a question as defined by the foreign key
class Choice(models.Model):
    # Fields 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #Methods
    def __str__(self):
        return self.choice_text


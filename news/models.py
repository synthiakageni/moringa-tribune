from django.db import models
from django.db.models.fields import CharField
import datetime as dt
# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self) :
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = models.CharField(max_length = 60)
    editor = models.ForeignKey(
        Editor,
        on_delete=models.CASCADE
        )
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')


#Testing Save method
    def test_save_Method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) >0) 

    @classmethod
    def today_news(cls):
        today = dt.date.today()
        news =cls.objects.filter(pub_date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news= cls.objects.filter(pub_date=date)
        return news


    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    



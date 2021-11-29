from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.james=Editor(first_name = 'james', last_name = 'Muriuki',email = 'james@moringaschool.com')

#Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

class ArticleTestClass(TestCase):
    def setUp(self):
        #creating a new editor and saving it
        self.james= Editor(first_name ='james',last_name='Muriuki',email='james@moringaschool.com')
        self.james.save_editor()

        #creating a new tag an dsaving it
        self.new_tag=tags(name='testing')
        self.new_tag.save()

        self.new_article=Article(title='Test Article',post ='This is a random test post',editor= self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete() 

    def test_get_news_today(self):
        today_news=Article.today_news()
        self.assertTrue(len(today_news)>0) 

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date= dt.datetime.strptime(test_date, '%Y-%m-%d').date()  
        news_by_date= Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)        

        



 
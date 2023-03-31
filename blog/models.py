from django.db import models

# Create your models here.

class Post(models.Model): #из пакета models наследуемся у класса Model
	#наш Post class это подкласс класса Model
	#Post класс наследует всю функциональность класса Model
	#Функциональность из класса Model нам нужна для сохранения информации из класса Post в базу данных
	#Класс Post теперь будет автоматически сохраняться в базе данных - так как мы унаследовались от класса Model

	#Берем модели от сюда: https://docs.djangoproject.com/en/4.1/ref/models/fields/#
	title = models.CharField(max_length=300)
	date = models.DateTimeField()
	text = models.TextField()
	image = models.ImageField(upload_to='event_images/')
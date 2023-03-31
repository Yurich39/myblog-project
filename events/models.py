from django.db import models

# Create your models here.

class Event(models.Model): #из пакета models наследуемся у класса Model
	#наш Event class это подкласс класса Model
	#Event класс наследует всю функциональность класса Model
	#Функциональность из класса Model нам нужна для сохранения информации из класса Event в базу данных
	#Класс Event теперь будет автоматически сохраняться в базе данных - так как мы унаследовались от класса Model

	event_image = models.ImageField(upload_to='event_images/')
	event_text = models.CharField(max_length=300)


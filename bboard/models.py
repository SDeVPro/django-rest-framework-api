from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
# class AdvUser(models.Model):
#     is_activated = models.BooleanField(default=True)
#     user = models.OneToOneField(User,on_delete=models.CASCADE)

# class Spare(models.Model):
#     name = models.CharField(max_length=30)
# class Machine(models.Model):
#     name = models.CharField(max_length=30)
#     spares = models.ManyToManyField(Spare)
class Rubric(models.Model):
    name = models.CharField(max_length=200)
    # def get_first_rubric():#bu funksiya 1-yaratilgan rubrikaga bog'liq bo'ladi va shuni qaytaradi
    #     return Rubric.objects.first()

    def __str__(self):
        return self.name

# class Bb(models.Model):
#     KINDS = (
#     ('Sotib-Sotibolish',(
#         ('b','Sotib olaman'),
#         ('s','Sotaman'),
#     )),
#     ('Almashtirish',(
#         ('c','Almashtiraman'),
#     ))
#     )    
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     kind = models.CharField(max_length=1,choices=KINDS,default='s')
#     #rubric = models.ForeignKey(Rubric,on_delete=models.SET(get_first_rubric))#bu yerda har qanday yaratiladigan e'lon olib kelingan 1-rubrikaga bog'liq bo'lib qoladi
#     #rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT,limit_choices_to={'show':True})#bu Rubrikadagi ma'lumot o'chganda ham e'lon qoladi, bu bazada ortiqcha joyni egallash bo'ladi
#     # rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT,related_name='entries')
#     # first_rubric = Rubric.objects.first()
#     # bbs = first_rubric.entries.all()
#     # rubric = models.ForeignKey(Rubric,on_delete=models.PROTECT,related_query_name='entry')
#     # rubrics = Rubric.objects.filter(entry__title='Uy')
#     #rubric = models.ForeignKey(Rubric, on_delete=models.OneToOneField)#birga bir ulanish asosan mijozga nisbatan ishlatiladi
# class Bbs(models.Model):
#     class Kinds(models.IntegerChoices):
#         BUY = 1, 'Sotibolish'
#         SELL = 2,'Sotish'
#         EXCHANGE = 3, 'Almashtiraman'
#         RENT = 4

#     kind = models.SmallIntegerField(choices=Kinds.choices, default=Kinds.SELL)

# class Measure(models.Model):
#     class Measurements(float,models.Choices):
#         METERS = 1.0, 'Metr'
#         FEET = 0.3048, 'Fut'
#         YARDS = 0.9144, 'Yard'
#     measurement = models.FloatField(choices=Measurements.choices) 



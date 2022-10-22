from django.db import models


class Date(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return f'{self.date}'


class DataTable(models.Model):
    name = models.CharField('Наименование сырья', max_length=100)
    count_iron = models.FloatField('Содержание железа')
    count_silicon = models.FloatField('Содержание кремния')
    count_aluminum = models.FloatField('Содержание алюминия')
    count_calcium = models.FloatField('Содержание кальция')
    count_sulfur = models.FloatField('Содержание серы')
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

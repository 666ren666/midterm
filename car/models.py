from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    class CarType(models.TextChoices):
        CAR = 'C', 'Car'
        TRUCK = 'T', 'Truck'
        MOTORCYCLE = 'M', 'Motorcycle'

    cartype = models.CharField(max_length=3, choices=CarType.choices, default=CarType.CAR)
    number = models.CharField(max_length=20, null=False)
    manufacturer = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True,
                              default='car.png')

    def __str__(self):
        typed = self.get_cartype_display()
        return f'{typed} - {self.number}'

class Employee(User):
    class Meta:
        verbose_name = 'Employee'

    tagnumber = models.CharField(max_length=50)

class Treatment(models.Model):
    class TreatmentType(models.IntegerChoices):
        TEN_TOUSAND = 1, '10,000'
        BREAKS = 2, 'BREAKS'
        THIRTY_THOUSAND = 3, '30,000'        
    type = models.IntegerField(choices=TreatmentType.choices, null=False),
    price = models.DecimalField(decimal_places=2, max_digits=10 ,null=False),
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)





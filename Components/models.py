from django.db import models
import os

def upload_path_products(instance, filename):
    path=f'Product_Images/{instance.Type}'
    return os.path.join(path, filename)


class Product(models.Model):

    TYPE_CHOICES = [
	('Resistor', 'Resistor'),
	('Capacitor', 'Capacitor'),
	('Inductor', 'Inductor'),
	('Transformer', 'Transformer'),
	('Transistor', 'Transistor'),
	('IC', 'IC'),
	('Thyristor', 'Thyristor'),
	('Diode', 'Diode'),
	('Amplifier', 'Amplifier'),
	('Relay', 'Relay'),
	('Switch', 'Switch'),
	('Motor', 'Motor'),
	('Solenoid', 'Solenoid'),
	('Actuator', 'Actuator'),
	('LCD', 'LCD'),
	('LED', 'LED'),
	('OLED', 'OLED'),
	('TFT', 'TFT'),
	('TouchScreen', 'TouchScreen'),
	('Temperature', 'Temperature'),
	('Pressure', 'Pressure'),
	('Motion', 'Motion'),
	('Light', 'Light'),
	('Gas', 'Gas'),
    ]


    Type=models.CharField(max_length=20, choices=TYPE_CHOICES,null=True)
    P_name = models.CharField(max_length=50, verbose_name="Product Name")
    Bundle_set = models.PositiveIntegerField(default=1)  
    Price = models.DecimalField(max_digits=10, decimal_places=2)  
    heading = models.CharField(max_length=100)
    P_image = models.ImageField(upload_to=upload_path_products, blank=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    content5 = models.TextField(blank=True)
    background_image = models.ImageField(upload_to=upload_path_products, blank=True)
    image1 = models.ImageField(upload_to=upload_path_products, blank=True)
    image2 = models.ImageField(upload_to=upload_path_products, blank=True)
    image3 = models.ImageField(upload_to=upload_path_products, blank=True)
    image4 = models.ImageField(upload_to=upload_path_products, blank=True)
    image5 = models.ImageField(upload_to=upload_path_products, blank=True)
    
    def __str__(self):
        return self.P_name

    

class Passive(models.Model):
    type=models.CharField(max_length=20,unique=True)
    heading = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='Passive/')
    para1 = models.TextField()
    image1 = models.ImageField(upload_to='Passive/')
    para2 = models.TextField()
    h2 = models.CharField(max_length=50)
    para3 = models.TextField()
    image2 = models.ImageField(upload_to='Passive/')

    def __str__(self):
        return self.type


class Active(models.Model):
    type=models.CharField(max_length=20,unique=True)
    heading = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='Active/')
    para1 = models.TextField()
    image1 = models.ImageField(upload_to='Active/')
    h2 = models.CharField(max_length=50)
    para2 = models.TextField()
    image2 = models.ImageField(upload_to='Active/')
    para3 = models.TextField()
    h3=models.CharField(max_length=50)
    para4 = models.TextField()
    image3 = models.ImageField(upload_to='Active/')

    def __str__(self):
        return self.type

class BaseComponents(models.Model):
    type=models.CharField(max_length=20,unique=True)
    heading = models.CharField(max_length=100)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    content5 = models.TextField(blank=True)

    def __str__(self):
        return self.type

    class Meta:
        abstract = True


class Electromechanical(BaseComponents):
    background_image = models.ImageField(upload_to='Electromechanical/',blank=True)
    image1 = models.ImageField(upload_to='Electromechanical/',blank=True)
    image2 = models.ImageField(upload_to='Electromechanical/',blank=True)
    image3 = models.ImageField(upload_to='Electromechanical/',blank=True)
    image4 = models.ImageField(upload_to='Electromechanical/',blank=True)
    image5 = models.ImageField(upload_to='Electromechanical/',blank=True)
    
    def __str__(self):
        return self.type

class Display(BaseComponents):
    background_image = models.ImageField(upload_to='Display/',blank=True)
    image1 = models.ImageField(upload_to='Display/',blank=True)
    image2 = models.ImageField(upload_to='Display/',blank=True)
    image3 = models.ImageField(upload_to='Display/',blank=True)
    image4 = models.ImageField(upload_to='Display/',blank=True)
    image5 = models.ImageField(upload_to='Display/',blank=True)
    
    def __str__(self):
        return self.type


class Sensor(BaseComponents):
    background_image = models.ImageField(upload_to='Sensor/',blank=True)
    image1 = models.ImageField(upload_to='Sensor/',blank=True)
    image2 = models.ImageField(upload_to='Sensor/',blank=True)
    image3 = models.ImageField(upload_to='Sensor/',blank=True)
    image4 = models.ImageField(upload_to='Sensor/',blank=True)
    image5 = models.ImageField(upload_to='Sensor/',blank=True)
    
    def __str__(self):
        return self.type


def upload_path(instance, filename):
    path=f'Component_Images/{instance.Category}'
    return os.path.join(path, filename)

class Component(models.Model):
        
	CATEGORY_CHOICES = [
	('Active', 'Active'),
	('Passive', 'Passive'),
	('ElectroMechanical', 'ElectroMechanical'),
	('Display', 'Display'),
	('Sensor', 'Sensor'),]
	
	    
	Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
	Type = models.CharField(max_length=20,unique=True)
	heading = models.CharField(max_length=100)
	content1 = models.TextField(blank=True)
	content2 = models.TextField(blank=True)
	content3 = models.TextField(blank=True)
	content4 = models.TextField(blank=True)
	content5 = models.TextField(blank=True)
	background_image = models.ImageField(upload_to=upload_path, blank=True)
	image1 = models.ImageField(upload_to=upload_path, blank=True)
	image2 = models.ImageField(upload_to=upload_path, blank=True)
	image3 = models.ImageField(upload_to=upload_path, blank=True)
	image4 = models.ImageField(upload_to=upload_path, blank=True)
	image5 = models.ImageField(upload_to=upload_path, blank=True)
     
	def __str__(self):	
	    return f"{self.Category} - {self.Type}"


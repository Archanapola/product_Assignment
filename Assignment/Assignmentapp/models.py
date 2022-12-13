from django.db import models

# Create your models here.
SIZE=(
('10','10'),
('20','20'),
('30','30'),
)

QUALITY=(
('HIGH','High'),
('LOW','Low'),
('MEDIUM','Medium')
)
class productMainModel(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    price=models.DecimalField()
    unique_code=models.UUIDField(primary_key=True)
    size=models.IntegerField(choices=SIZE)
    quality=models.CharField(choices=QUALITY)
def __str__(self):
    return self.productMainModel

COLOUR=(
('RED','Red'),
('BLUE','Blue'),
('GREEN','Green'),
('BLACK','Black'),
)
class productColourModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    colour=models.CharField(choices=COLOUR)
class productImageModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    image=models.ImageField()

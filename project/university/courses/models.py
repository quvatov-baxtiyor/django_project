from django.db import models

# Create your models here.
class Special(models.Model):
    name = models.CharField(max_length=512)
    code = models.SlugField(max_length=512, unique=True)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.name



class Teacher(models.Model):
    DEGREE1 = "Master"
    DEGREE2 = "Secondary"
    LEVEL = (
        (DEGREE1, "Master"),
        (DEGREE2, "Secondary")
    )

    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    degree = models.CharField(max_length=512,choices=LEVEL)

    def __str__(self):
        return f"The {self.degree} degree teacher {self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=512)
    specialities = models.ManyToManyField(Special)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"Subject name: {self.name}"

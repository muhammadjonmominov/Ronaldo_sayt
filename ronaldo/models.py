from django.db import models


class About_1(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/abouts')
    date_of_birth = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name



class Education_1(models.Model):
    title = models.CharField(max_length=100)
    year_range = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    discription = models.TextField()
    def __str__(self):
        return self.title
    

class Experience_1(models.Model):
    title = models.CharField(max_length=100)
    year_range = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    discription = models.TextField()
    def __str__(self):
        return self.title
    


class Skill_1(models.Model):
    name = models.CharField(max_length=50)  
    percent = models.PositiveIntegerField()  
    last_week = models.PositiveIntegerField(default=28)
    last_month = models.PositiveIntegerField(default=60)

    def __str__(self):
        return self.name
    



class Awards_1(models.Model):
    title = models.CharField(max_length=100)
    year_range = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    discription = models.TextField()
    def __str__(self):
        return self.title
    




class Project_1(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='projects/')  

    def __str__(self):
        return self.title



class Counter_1(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}: {self.number}"





class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

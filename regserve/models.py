##Data models file (schemas).

from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator

#Person Schema
class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    idnumber = models.PositiveBigIntegerField()
    email = models.EmailField(blank=True)
    datecreated = models.DateTimeField(blank=True, auto_now_add=True)
    datemodified = models.DateTimeField(blank=True, auto_now=True)

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        abstract = True

    def __str__(self):
        return f'ID: {self.id}: Name: {self.full_name}, Student id: {self.idnumber}, Email: {self.email}, Date Created: {self.datecreated}, Date Modified: {self.datemodified}'

##Student Schema
class Student(Person):
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophmore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    
    MAJORS = [
        ('CS', 'Computer Science'),
        ('ENG', 'Engineering'),
        ('BUS', 'BUSINESS'),
        ('SC', 'Science'),
        ('LAW', 'Law'),
        ('NUR', 'Nursing'),
        ('UND', 'Undecided'),
    ]

    schoolyear = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL)
    major = models.CharField(max_length=3, choices=MAJORS)
    gpa = models.FloatField(max_length=4, blank=True)

    ## outputs a string of the object that is passed.
    def __str__(self):
        return f'ID: {self.id}: {super(Student, self).__str__()}, School Year: {self.schoolyear}, Major: {self.major}, GPA: {self.gpa}'
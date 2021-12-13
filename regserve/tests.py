from django.test import TestCase, Client
from .models import *
import io

##Test cases for below test assertions.
class DataTest(TestCase):
    def setUp(self):
        student1 = Student.objects.create(
            firstname="First",
            lastname="Student",
            idnumber=100,
            email="first@student.edu",
            schoolyear="FR",
            major="ENG",
            gpa=4.0, 
        )

        student2 = Student.objects.create(
            firstname="Second",
            lastname="Student",
            idnumber=101,
            email="second@student.edu",
            schoolyear="SR",
            major="ENG",
            gpa=2.0,
        )
        self.test_client = Client()

    ##Testing API
    def test_student_api(self):
        student_response = self.test_client.get('/registration/data/students/')
        print(f'TEST_STUDENT_API: api response is: {student_response} and the status is {student_response.status_code}')
        print(f'TEST_STUDENT_API: api response content is: {student_response.content}')
        student_stream = io.BytesIO(student_response.content)

    ##Testing web client.
    def test_student(self):
        student_list = Student.objects.all()
        for student in student_list:
            print(f'Inside test student: student is {student}')
            if(student.id == 1):
                self.assertEqual(student.full_name, 'First Student')
                self.assertEqual(student.idnumber, 100)



class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_response(self):
        response = self.test_client.get('/regserve')
        print(f'In simple test, response is {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world from django backend')
    


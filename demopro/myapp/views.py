from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View


# Create your views here.

#API view

class GoodMorning(View):
    def get(self,request):
        data={"Message":"Good Morning"}
        return JsonResponse(data)

class HelloWorld(View):
    def get(self,request):
        data={"Message":"Hello World"}
        return JsonResponse(data)

class GoodEvening(View):
    def get(self,request):
        data = {"Message": "Good Evening"}
        return JsonResponse(data)





class UserDetails(View):
    def get(self,request):
        data=[

        {'name':'arun','age':23,'place':'ekm'},
        {'name': 'Amal', 'age': 24, 'place': 'tvm'},
        {'name': 'Anu', 'age': 25, 'place': 'ekm'},
        ]

        return JsonResponse(data,safe=False)


from .models import Student
#API view for reading all student records
class StudentList(View):
    def get(self,request):
        s = Student.objects.all()  # gets all records
        print(s)
        print(type(s))

        s=Student.objects.all().values()   #converts each objects into dictionary
        print(s)
        print(type(s))  #Queryset of student objects

        data=list(s)   #converts Queryset into list format
        print(data)
        print(type(data))

        return JsonResponse(data,safe=False)


from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#API view for creating a new student record

@method_decorator(csrf_exempt,name='dispatch')
class StudentCreate(View):
    def post(self,request):

        data=loads(request.body)  #converts json data into python native types

        r=data['rollnumber']
        n=data['name']
        a=data['age']
        p=data['place']
        m=data['marks']

        s=Student.objects.create(rollnumber=r,name=n,age=a,place=p,marks=m)
        s.save()

        return JsonResponse({"message":"Inserted Data Successfully"})


#API view for reading a specific record
class StudentDetail(View):
    def get(self,request,i):
        s=list(Student.objects.filter(id=i).values()) #json to dictionary
        if s:
            return JsonResponse(s,safe=False)
        else:
            return JsonResponse({'message':'No Student Data'})


@method_decorator(csrf_exempt,name="dispatch")
class StudentDelete(View):
    def delete(self,request,i):
        s=Student.objects.get(id=i)
        s.delete()
        return JsonResponse({'message':'Deleted Successully'})



import json
@method_decorator(csrf_exempt,name="dispatch")
class Studentfullupdate(View):
    def put(self,request,i):            #request.body - data coming from client app
        data=json.loads(request.body)   #loads used to translate coming json data into
                                        #python native/dictionary
        print(data)
        try:
            s=Student.objects.get(id=i)

            s.rollnumber=data['rollnumber']
            s.name=data['name']
            s.age=data['age']
            s.place=data['place']
            s.marks=data['marks']
            s.save()

            return JsonResponse({'message':'updated successfully'})
        except:
            return JsonResponse({'messsage':'No student data'})


@method_decorator(csrf_exempt,name="dispatch")
class Studentpartialupdate(View):
    def patch(self,request,i):
        data=json.loads(request.body)
        try:
            s = Student.objects.get(id=i)
            if 'rollnumber' in data:
                s.rollnumber=data['rollnumber']
            if 'name' in data:
                s.name=data['name']
            if 'age' in data:
                s.age=data['age']
            if 'place' in data:
                s.place=data['place']
            if 'marks' in data:
                s.marks=data['marks']
            s.save()

            return JsonResponse({'message':'updated Partially'})
        except:
            return JsonResponse({'messsage':'No student data'})


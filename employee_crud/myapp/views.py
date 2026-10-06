from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Employee

@method_decorator(csrf_exempt, name='dispatch')
# API view for reading all employee records
class EmployeeList(View):

    def get(self, request):

        e=Employee.objects.all().values()
        data=list(e)

        return JsonResponse(data, safe=False)


# API view for creating a new employee record
from json import loads
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCreate(View):
    def post(self,request):

        data=loads(request.body)  #converts json data into python native types

        # e=data['empid']
        # n=data['name']
        # a=data['age']
        # p=data['place']
        # g=data['gender']
        # j=data['joining_date']
        # s=data['salary']
        # d=data['designation']

        e=Employee.objects.create(**data)
        e.save()

        return JsonResponse({"message":"Inserted Data Successfully"})


# API view for reading a specific employee record
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetail(View):
    def get(self,request,i):
        e=list(Employee.objects.filter(id=i).values()) #json to dictionary
        if e:
            return JsonResponse(e,safe=False)
        else:
            return JsonResponse({'message':'No Student Data'})


# API view for deleting an employee record
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeDelete(View):
    def delete(self,request,i):
        e=Employee.objects.get(id=i)
        e.delete()
        return JsonResponse({'message':'Deleted Successully'})


# API view for full update
import json
@method_decorator(csrf_exempt,name="dispatch")
class Employeefullupdate(View):
    def put(self,request,i):            #request.body - data coming from client app
        data=json.loads(request.body)   #loads used to translate coming json data into
                                        #python native/dictionary
        print(data)
        try:
            e=Employee.objects.get(id=i)

            e.empid=data['empid']
            e.name=data['name']
            e.age=data['age']
            e.place=data['place']
            e.gender=data['gender']
            e.joining_date=data['joining_date']
            e.salary=data['salary']
            e.designation=data['designation']
            e.save()

            return JsonResponse({'message':'updated successfully'})
        except:
            return JsonResponse({'messsage':'No student data'})


# API view for partial update
@method_decorator(csrf_exempt,name="dispatch")
class Employeepartialupdate(View):
    def patch(self,request,i):
        data=json.loads(request.body)
        try:
            e = Employee.objects.get(id=i)
            if 'empid' in data:
                e.empid=data['empid']
            if 'name' in data:
                e.name=data['name']
            if 'age' in data:
                e.age=data['age']
            if 'place' in data:
                e.place=data['place']
            if 'gender' in data:
                e.gender=data['gender']
            if 'joining_date' in data:
                e.joining_date=data['joining_date']
            if 'salary' in data:
                e.salary=data['salary']
            if 'designation' in data:
                e.designation=data['designation']
            e.save()

            return JsonResponse({'message':'updated Partially'})
        except:
            return JsonResponse({'messsage':'No student data'})
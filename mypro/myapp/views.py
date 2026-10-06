from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def first(request):
#     if(request.method=="GET"):
#         return HttpResponse("First Page")
#
# def second(request):
#     if (request.method == "GET"):
#         return HttpResponse("Second Page")

from django.views import View

# class First(View):
#     def get(self,request):
#         return HttpResponse("""
#
#         <h1>First Page</h1>
#         <h1>hello</h1>
#
#         """)

from myapp.models import Person
class First(View):
    def get(self,request):
        # data=[{"name":"Arun","age":23,"place":"ekm"},
        #       {"name": "Amal", "age": 28, "place": "tvm"},
        #       {"name": "Anu", "age": 21, "place": "tcr"}]

        data=Person.objects.all()


        context={'data':data}
        return render(request,'first.html',context)
                       #context sends data from view to templates

# class Second(View):
#     def get(self,request):
#         return HttpResponse("<h1>Second Page</h1>")


class Second(View):
    def get(self,request):
        data={"name":"Manu","age":28,"place":"tvm"}
        return render(request,'second.html',context=data)

from myapp.models import Movie
class Movie_list(View):
    def get(self, request):
        m=Movie.objects.all()
        print(m)
        context={'movies':m}
        return render(request, 'movielist.html',context)


class Add_movie(View):
    def get(self, request):
        return render(request, 'addmovie.html')

    def post(self,request):
        print(request.POST)

        data=request.POST   #submitted data
        n=data['name']
        d=data['director']
        y=data['year']
        print(n,d,y)

        #Query for creating a new record in ORM
        #modelname.objects.create(column=value,column=value,column=value)

        m=Movie.objects.create(name=n,director=d,year=y)
        m.save()

        return render(request,'addmovie.html')
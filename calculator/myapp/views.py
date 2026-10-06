from django.shortcuts import render
from django.views import View
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Add(View):
    def get(self, request):
        return render(request, 'add.html')

    def post(self, request):

        data = request.POST  # submitted data
        n1 = int(data['n1'])
        n2 = int(data['n2'])

        s=n1+n2
        print(s)
        context={'result':s}

        return render(request, 'add.html',context)

class Fact(View):
    def get(self, request):
            return render(request, 'fact.html')

    def post(self, request):

        data = request.POST  # submitted data
        n1 = int(data['n1'])

        f = 1

        for i in range(1, n1 + 1):
            f = f * i
        print(f)
        context={'result':f}

        return render(request, 'fact.html',context)

class Bmi(View):
    def get(self, request):
        return render(request, 'bmi.html')

    def post(self, request):
        data = request.POST

        weight = float(data['weight'])
        height = float(data['height'])

        bmi = weight / (height * height)

        context = {'result': bmi}

        return render(request, 'bmi.html', context)
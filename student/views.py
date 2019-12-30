from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from student.models import Student
from student.froms import  StudentFrom

class IndexView(View):
    template_name = 'index.html'
    def index(self):
        students = Student.get_all()


    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentFrom()
        context.update({

            'form':form
        }
        )
        return  render(request,self.template_name,context=context)
    def post(self,request):
        form =StudentFrom(request.Post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
                'form':form
            })
        return render(request,self.template_name,context=context)


###
#def index(request):
#    students = Student.objects.all()
#    if request.method =='Post':
#        form = StudentFrom(request.Post)
#        if form.is_valid():
#            cleaned_data = form.cleaned_data
#            student = Student()
#            student.name = cleaned_data['name']
#            student.sex = cleaned_data['sex']
#            student.email = cleaned_data['email']
#            student.profession = cleaned_data['profession']
#            student.qq = cleaned_data['qq']
#            student.phone = cleaned_data['phone']
#            student.save()
#            return HttpResponseRedirect(reverse('index'))
#    else:
#        form = StudentFrom()
#
#    context = {
#        'students':students,
#        'form':form,
#   }
#    return render(request,'index.html', context=context)


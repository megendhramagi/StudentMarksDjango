from django.shortcuts import render,redirect
from .forms import MarkForm
from .models import StuMarks

# Create your views here.
def index(request):
    context = {
        'mark_form':MarkForm()
    }
    if request.method=="POST":
        mark_form_vals= MarkForm(request.POST)
        if mark_form_vals.is_valid():
            mark_form_vals.save()
    return render(request,'index.html',context)

def stu_marks(request):
    context = {
        'all_stu':StuMarks.objects.all()
    }
    return render(request,'stu_marks.html',context)

def markmodify(request):
    context={
        "mark_form":MarkForm()
    }
    if request.method=="POST":
        global id
        id = request.POST.get('id')
        mark_val = StuMarks.objects.get(id=id)
        context={
            "id":{'sid':id},
            "mark_form":MarkForm(instance=mark_val)
        }

    return render(request,'MarkModify.html',context)

def markupdate(request):
    if request.method=="POST":
        mark_val = StuMarks.objects.get(id=id)
        update = MarkForm(request.POST,instance=mark_val)
        if(update.is_valid()):
            update.save()
    return redirect('/inventory/stumarks/')


def markdelete(request, id):
    mark_val = StuMarks.objects.get(id = id)
    mark_val.delete()
    return redirect('/inventory/stumarks/')





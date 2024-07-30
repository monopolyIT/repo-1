from django.shortcuts import render

# Create your views here.
from datetime import *
from .models import *

def empdata(req):
    data1=Employee.objects.filter(status=True)
    if req.method=='POST' and 'submit' in req.POST:
        Empid=req.POST.get('Empid')
        Empname=req.POST.get('Empname')
        Empjoin=req.POST.get('joindate')
        print("records :",Empid,Empname,Empjoin)
        Employee.objects.create(
            EmployeeId=Empid,
            EmpName=Empname,
            EmpJoindate=datetime.now(),
            status=True,
        ).save()
    if req.method=='POST' and 'delete' in req.POST:
        Empid=req.POST.get('id')
        print(Empid)
        Employee.objects.filter(id=Empid).delete()
    if req.method=='POST' and 'Update' in req.POST:
        id=req.POST.get('id')
        empid=req.POST.get('Empid')
        empname=req.POST.get('Empname')
        print("data :",id,empid,empname)
        Employee.objects.filter(id=id).update(
            EmployeeId=empid,
            EmpName=empname,
        )
    context={
            'data':data1,
            }
    return render(req,"index.html",context)
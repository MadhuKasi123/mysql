from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import *
# Create your views here.

def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]
    
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)


def selfjions(request):
    empobjectmanager=Emp.objects.select_related('mgr').all()
    empobjectmanager=Emp.objects.select_related('mgr').filter(Q(mgr=7698)|Q(mgr=7902))
    empobjectmanager=Emp.objects.select_related('mgr').filter(deptno__deptno=20)
    empobjectmanager=Emp.objects.select_related('mgr').filter(deptno__deptno=20,mgr__ename='JONES')
    empobjectmanager=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    empobjectmanager=Emp.objects.select_related('mgr').filter(mgr__ename='KING',sal__gte=2500)
    empobjectmanager=Emp.objects.select_related('mgr').filter(mgr=7698)
    empobjectmanager=Emp.objects.select_related('mgr').filter(mgr__ename='KING',sal__gte=2500)
    empobjectmanager=Emp.objects.select_related('mgr').filter(Q(ename='SMITH')|Q(ename='FORD'))
    empobjectmanager=Emp.objects.select_related('mgr').filter(Q(deptno__deptno=10)|Q(deptno__deptno=30))
    empobjectmanager=Emp.objects.select_related('mgr')[2:6:]
    empobjectmanager=Emp.objects.select_related('mgr').filter(empno=7788)
    empobjectmanager=Emp.objects.select_related('mgr').filter(mgr__empno=7566)
    empobjectmanager=Emp.objects.select_related('mgr').filter(mgr__empno=7698,job='SALESMAN')
    empobjectmanager=Emp.objects.select_related('mgr').all()
    d={'empobjectmanager':empobjectmanager}
    return render(request,'selfjions.html',d)




def Emp_Mgr_Dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='ALLEN')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH') | Q(deptno=10))
    emd=Emp.objects.select_related('mgr').filter(mgr=7698)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__empno=7566)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__empno=7698,job='OPERTIONS')
    emd=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    emd=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    emd=Emp.objects.select_related('mgr').filter(Q(ename='SMITH')|Q(ename='MARTIN'))
    emd=Emp.objects.select_related('mgr').filter(deptno__deptno=20)
    emd=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    emd=Emp.objects.select_related('mgr','deptno')[2:6:]
    emd=Emp.objects.select_related('mgr')[:3:2]
    emd=Emp.objects.select_related('deptno','mgr').all().order_by('-ename')
    emd=Emp.objects.select_related('deptno','mgr').all().order_by('ename')
    emd=Emp.objects.select_related('deptno','mgr').all().order_by('-ename')[:3:]
    emd=Emp.objects.select_related('deptno','mgr').all().order_by('ename')[:3:]
    emd=Emp.objects.select_related('mgr').filter(sal__lte=1000)
    emd=Emp.objects.select_related('mgr').filter(Q(mgr=7654)|Q(mgr=7566))
    emd=Emp.objects.select_related('deptno').filter(hiredate__year=2023,sal__lte=1450)
    emd=Emp.objects.select_related('mgr','deptno').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('mgr','deptno').filter(mgr__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr','deptno').filter(deptno__dlocation='NEWYORK')
    emd=Emp.objects.select_related('mgr','deptno').filter(ename__endswith='s')
    emd=Emp.objects.select_related('deptno','mgr','deptno').filter(ename__startswith='B')
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dlocation__startswith='N')
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dlocation__endswith='O')
    emd=Emp.objects.select_related('mgr').filter(Q(deptno__deptno=20) | Q(deptno__deptno=40))
    emd=Emp.objects.select_related('mgr').filter(Q(deptno__deptno=30) | Q(deptno__deptno=20))
    emd=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gte=1450)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH')|Q(deptno__dname='SALES'))
    emd=Emp.objects.select_related('deptno','mgr').all().order_by(Length('ename'))[:4]
    emd=Emp.objects.select_related('deptno','mgr').all().order_by(Length('ename'))[4::3]
    
    d={'emd':emd}
    return render(request,'Emp_Mgr_Dept.html',d)
def Emp_sal(request):
    
    EO=Emp.objects.all()
    SO=SalGrade.objects.all()
    SO=SalGrade.objects.filter(grade=4)#[grade4 SalgradeObjects]
    EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    SO=SalGrade.objects.filter(grade__in=(3,4))

    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))


    d={'EO':EO,'SO':SO}
    return render(request,'Emp_sal.html',d)
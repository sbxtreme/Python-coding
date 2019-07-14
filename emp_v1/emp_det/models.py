from django.db import models

class EmployeeDetail(models.Model):
    empno = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    mgr = models.CharField(max_length=200)
    hiredate = models.DateTimeField('Hire date')
    sal = models.IntegerField()
    commission = models.IntegerField()
    deptno = models.IntegerField()
    dname= models.CharField(max_length=100)
    loc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'employee_detail'
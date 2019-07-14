from django.contrib import admin
from import_export.admin import ExportMixin
from . models import EmployeeDetail

class EmployeeDetAdmin(ExportMixin,admin.ModelAdmin):
	list_display = ('empno','ename','designation','mgr','hiredate','sal','commission','deptno','dname','loc')
	list_per_page = 5
	list_display_links = None
	list_filter = ("hiredate","dname","loc")

	# this will add filters
	def is_very_benevolent(self, obj):
		return obj.benevolence_factor

	# this will disable the add functionality
	def has_add_permission(self, request):
		return False

	# this will disable the delete functionality
	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(EmployeeDetail,EmployeeDetAdmin)
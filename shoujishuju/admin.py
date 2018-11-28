from django.contrib import admin
from .models import DataTable

# Register your models here.
#@admin.register(DataTable)
# class KhpjAdmin(admin.ModelAdmin):
# 	"""docstring for khpjAdmin"""
# 	list_display = ('name', 'mobile', 'service', 'waiting_time', 'overall_satisfaction', 'attitude', 'cycle', 'eat', 'proposal', 'add_time')
# 	list_filter = ('add_time')

admin.site.register(DataTable)

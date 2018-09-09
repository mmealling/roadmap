from django.contrib import admin

# Register your models here.
from dependency.models import Tasks, Customer, Vendor, Predecessors, Successors, Tags, Movie, Book

# Define the admin class
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('elementID', 'name', 'owner')

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Predecessors)
admin.site.register(Successors)
admin.site.register(Tags)
admin.site.register(Movie)
admin.site.register(Book)


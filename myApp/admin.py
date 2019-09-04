from django.contrib import admin
from .models import Home
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','list_date','realtor','status',)
    list_display_links = ('id', 'title',)
    list_filter = ('realtor','status','list_date')
    search_fields = ('title','city','district','price')
    list_editable = ('status',)
    list_per_page = 25
    prepopulated_fields = {'slug':('title',)}




admin.site.register(Home, HomeAdmin)

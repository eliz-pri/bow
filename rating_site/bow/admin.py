from django.contrib import admin
from bow.models import Restaurant,UserBW2
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('res_name','location')


admin.site.register(Restaurant,RestaurantAdmin)


class UserBWAdmin(admin.ModelAdmin):
	list_display = ('user','btr_res','wrs_res')


admin.site.register(UserBW2,UserBWAdmin)

class UserAdmin(admin.ModelAdmin):
	fields = ('name','email')
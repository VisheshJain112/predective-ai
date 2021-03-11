from django.contrib import admin
from .models import AD_User
from .models import AD_Admin
from django.contrib import admin
from user_ui.models import UserUiUserInput
# Register your models here.
admin.site.register(AD_User)
admin.site.register(AD_Admin)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('username','case_number','started_at','time_taken','prediction_1','prediction_2','prediction_3','recommendation_1','recommendation_2','recommendation_3')

admin.site.register(UserUiUserInput,HomeAdmin)



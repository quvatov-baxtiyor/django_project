from django.contrib import admin
from .models import Special,Teacher,Subject

# Register your models here.
@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    search_fields = ['name','code', ]
    list_display = ['name', 'code', 'start_date', 'is_active', ]
    list_filter = ['name',]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name',]
    list_display = ['first_name', 'last_name', 'degree', ]
    list_filter = ['degree',]


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]
    list_filter = ['name', ]
    autocomplete_fields = ['specialities','teachers' ]
admin.site.register(Subject,SubjectAdmin)

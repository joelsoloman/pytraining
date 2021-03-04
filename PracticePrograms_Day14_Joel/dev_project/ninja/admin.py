from django.contrib import admin

# Register your models here.
from .models import Developer, Skill

class SkillInLine(admin.StackedInline):
    model = Skill
    extra = 1

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'experience')
    fieldsets = [
        (None, {'fields':['name']}),
        ('country', {'fields':['country']}),
        ('experience', {'fields':['experience']}),
    ]
    inlines = [SkillInLine]

admin.site.register(Developer, DeveloperAdmin)
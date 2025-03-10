from django.contrib import admin
from .models import ContractTemplate, ContractInstance

class ContractTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'template_file', 'created_at')

class ContractInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'template', 'variables', 'created_at')

admin.site.register(ContractTemplate, ContractTemplateAdmin)
admin.site.register(ContractInstance, ContractInstanceAdmin)

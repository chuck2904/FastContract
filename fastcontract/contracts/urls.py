from django.urls import path
from . import views

urlpatterns = [
    path('create_instance/<int:template_id>/', views.create_contract_instance, name='create_contract_instance'),
    path('templates/', views.list_templates, name='list_templates'),
    # path('send/<int:instance_id>/', views.send_contract, name='send_contract'),
    path('display_template_pdf/<int:template_id>/', views.display_template_pdf, name='display_template_pdf'),
    path('download_template/<int:template_id>/', views.download_template, name='download_template'),
    path('contract-instances/', views.contract_instances, name='contract_instances'),
    path('download/<int:instance_id>/', views.download_contract_instance, name='download_contract_instance'),
    path('excel-like-table/', views.excel_like_table, name='excel_like_table'),
]

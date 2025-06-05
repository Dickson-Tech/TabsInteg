# filepath: c:\Users\Dickson.NENGA\Desktop\TabsInteg\Purchase_Order\urls.py
from django.contrib import admin
from django.urls import path
from PO_Data import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.supplier_list_view, name='supplier_list'),  # Root URL
    path('supplier_List_Form', views.supplier_create, name='supplier'),
    path('supplier_list', views.supplier_list, name='supplier_list'),
    #path('success', views.supplier_create, name='success'),  # Redirect after successful creation
    path('', views.supplier_list, name='home'), 
    path('supplier_edit/<int:pk>/', views.supplier_edit, name='supplier_edit'),
    path('supplier_delete/<int:pk>/', views.supplier_delete, name='supplier_delete'), # Delete a supplier


]
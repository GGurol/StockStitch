from django.urls import path, include
from . import views
from .views import api_router, notifications, mark_notification_read, CustomerLoginView, customer_dashboard, customer_invoice_pdf, order_qrcode, inventory_qrcode, orders_calendar, orders_ical
from rest_framework.authtoken.views import obtain_auth_token
<<<<<<< HEAD
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('customers/export/', views.customers_export, name='customers_export'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
=======

urlpatterns = [
    path('customers/export/', views.customers_export, name='customers_export'),
>>>>>>> c423afddd282a4f6806259664fced3dc995bee88
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.meeting_mode, name='meeting_mode'),
    path('customers/', views.customers, name='customers'),
    path('customers/edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('customers/import/', views.customers_import, name='customers_import'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/export/', views.inventory_export, name='inventory_export'),
    path('inventory/import/', views.inventory_import, name='inventory_import'),
    path('inventory/edit/<int:pk>/', views.edit_inventory, name='edit_inventory'),
    path('inventory/delete/<int:pk>/', views.delete_inventory, name='delete_inventory'),
    path('orders/', views.orders, name='orders'),
    path('orders/export/', views.orders_export, name='orders_export'),
    path('orders/export/excel/', views.orders_export_excel, name='orders_export_excel'),
    path('orders/edit/<int:pk>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:pk>/', views.delete_order, name='delete_order'),
    path('orders/import/', views.orders_import, name='orders_import'),
    path('requirements/', views.requirements, name='requirements'),
    path('requirements/export/', views.requirements_export, name='requirements_export'),
    path('requirements/edit/<int:pk>/', views.edit_requirement, name='edit_requirement'),
    path('requirements/delete/<int:pk>/', views.delete_requirement, name='delete_requirement'),
    path('requirements/import/', views.requirements_import, name='requirements_import'),
    path('payments/', views.payments, name='payments'),
    path('payments/export/', views.payments_export, name='payments_export'),
    path('payments/edit/<int:pk>/', views.edit_payment, name='edit_payment'),
    path('payments/delete/<int:pk>/', views.delete_payment, name='delete_payment'),
    path('payments/import/', views.payments_import, name='payments_import'),
    path('customers/export/excel/', views.customers_export_excel, name='customers_export_excel'),
    path('inventory/export/excel/', views.inventory_export_excel, name='inventory_export_excel'),
    path('requirements/export/excel/', views.requirements_export_excel, name='requirements_export_excel'),
    path('payments/export/excel/', views.payments_export_excel, name='payments_export_excel'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('suppliers/edit/<int:pk>/', views.edit_supplier, name='edit_supplier'),
    path('suppliers/delete/<int:pk>/', views.delete_supplier, name='delete_supplier'),
    path('purchases/', views.purchases, name='purchases'),
    path('purchases/edit/<int:pk>/', views.edit_purchase, name='edit_purchase'),
    path('purchases/delete/<int:pk>/', views.delete_purchase, name='delete_purchase'),
    path('analytics/', views.analytics, name='analytics'),
    path('history/<str:model_name>/<int:object_id>/', views.model_history, name='model_history'),
]
urlpatterns += [
    path('api/', include(api_router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('notifications/', notifications, name='notifications'),
    path('notifications/read/<int:pk>/', mark_notification_read, name='mark_notification_read'),
    path('customer/login/', CustomerLoginView.as_view(), name='customer_login'),
    path('customer/dashboard/', customer_dashboard, name='customer_dashboard'),
    path('customer/invoice/<int:order_id>/', customer_invoice_pdf, name='customer_invoice_pdf'),
    path('order/qrcode/<int:order_id>/', order_qrcode, name='order_qrcode'),
    path('inventory/qrcode/<int:item_id>/', inventory_qrcode, name='inventory_qrcode'),
    path('orders/calendar/', orders_calendar, name='orders_calendar'),
    path('orders/ical/', orders_ical, name='orders_ical'),
    path('sample/customers.csv', views.sample_customers_csv, name='sample_customers_csv'),
    path('sample/inventory.csv', views.sample_inventory_csv, name='sample_inventory_csv'),
    path('sample/orders.csv', views.sample_orders_csv, name='sample_orders_csv'),
    path('sample/requirements.csv', views.sample_requirements_csv, name='sample_requirements_csv'),
    path('sample/payments.csv', views.sample_payments_csv, name='sample_payments_csv'),
] 
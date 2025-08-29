from django.contrib import admin
from .models import Customer, InventoryItem, Order, Requirement, Payment, Supplier, Purchase, Notification, CustomerUser
from simple_history.admin import SimpleHistoryAdmin

# Unregister only if already registered
for model in [Customer, InventoryItem, Order, Requirement, Payment, Supplier, Purchase]:
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass

admin.site.register(Customer, SimpleHistoryAdmin)
admin.site.register(InventoryItem, SimpleHistoryAdmin)
admin.site.register(Order, SimpleHistoryAdmin)
admin.site.register(Requirement, SimpleHistoryAdmin)
admin.site.register(Payment, SimpleHistoryAdmin)
admin.site.register(Supplier, SimpleHistoryAdmin)
admin.site.register(Purchase, SimpleHistoryAdmin)
admin.site.register(Notification)
admin.site.register(CustomerUser)

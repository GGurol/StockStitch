from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import Customer, InventoryItem, Order, Requirement, Payment

class Command(BaseCommand):
    help = 'Set up default user roles and permissions.'

    def handle(self, *args, **options):
        # Define groups and their permissions
        roles = {
            'Admin': 'all',
            'Manager': ['add', 'change', 'view', 'delete'],
            'Staff': ['add', 'change', 'view'],
            'Viewer': ['view'],
        }
        models = [Customer, InventoryItem, Order, Requirement, Payment]
        for role, perms in roles.items():
            group, created = Group.objects.get_or_create(name=role)
            if perms == 'all':
                group.permissions.set(Permission.objects.all())
            else:
                allowed_perms = []
                for model in models:
                    ct = ContentType.objects.get_for_model(model)
                    for perm in perms:
                        codename = f'{perm}_{model._meta.model_name}'
                        try:
                            p = Permission.objects.get(content_type=ct, codename=codename)
                            allowed_perms.append(p)
                        except Permission.DoesNotExist:
                            pass
                group.permissions.set(allowed_perms)
            group.save()
        self.stdout.write(self.style.SUCCESS('Default roles and permissions set up successfully.')) 
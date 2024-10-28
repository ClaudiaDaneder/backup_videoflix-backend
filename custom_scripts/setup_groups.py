from django.contrib.auth.models import Group, Permission


customers_group, created = Group.objects.get_or_create(name='Customers')

internal_users_group, created = Group.objects.get_or_create(name='Internal Users')

change_customer_permission = Permission.objects.get(codename='change_customer')
delete_customer_permission = Permission.objects.get(codename='delete_customer')

internal_users_group.permissions.add(change_customer_permission, delete_customer_permission)

print('Groups and permissions created successfully')
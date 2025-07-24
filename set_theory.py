admins ={'Julie','Ronaldo', 'Mark', 'Samantha'}

editors = {'Julie', 'Mark'}

# combine both sets
all_users = admins.union(editors)
print(all_users)

# intersection of both sets
common_users = editors.intersection(admins)
print(common_users)

# admin users not in editors
admin_not_editors = admins.difference(editors)
print(admin_not_editors)
from os import environ as env

'''
Map of roles authorized to access endpoints
Only users with proper roles are authorized 
'''
auth_roles = {
    "view" : ['test', 'myrole']
}
def authorize_admin_user(user_roles):
    assert isinstance(user_roles,list) and user_roles != [], "No user roles found"

    assert 'admin' in user_roles, "No admin role found."
    print("You have full access to the application.")

authorize_admin_user(['admin','user'])

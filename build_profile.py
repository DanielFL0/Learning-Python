def make_profile(first, last, username):
    """Lets users make their own user profile with their information"""
    user = {}
    user['first_name'] = first.title()
    user['last_name'] = last.title()
    user['username'] = username
    return user


def show_user(user):
    """Displays the user information"""
    print("User information: \n")
    for key, value in user.items():
        print(key + ": " + value)

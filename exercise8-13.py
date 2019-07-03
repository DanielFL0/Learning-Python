#8-13 User profile: Start with a copy of user_profile.py from page 153.
#Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

#Using user_profile.py
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('daniel', 'saldana', 
                            location='monterrey', 
                            age=20, 
                            favorite_sport='soccer')
print(user_profile)

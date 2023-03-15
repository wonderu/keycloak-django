from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class NoNewUsersAccountAdapter(DefaultAccountAdapter):
    def login(self, request, user):
        return super(NoNewUsersAccountAdapter, self).login(request, user)
    
    def populate_username(self, request, user):
        return super(NoNewUsersAccountAdapter, self).populate_username(request, user)

    def save_user(self, request, user, form, commit=True):

        user = super(NoNewUsersAccountAdapter, self).save_user(request, user, form, commit=False)
        # user.voornaam = form.cleaned_data.get('first_name')
        # user.achternaam = form.cleaned_data.get('last_name')
        # user.user_group = form.cleaned_data.get('user_group')
        # user.save()
        # user.groups.add(user.user_group)
        # user.save()
        # if user.groups == 'group_b':
        #     user.is_active = False
        # else:
        #     user.is_active = True
        # user.save()
        return user
    
    
    
class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super(SocialAccountAdapter, self).populate_user(request, sociallogin, data)
        return user


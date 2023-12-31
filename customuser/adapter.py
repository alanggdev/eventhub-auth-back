from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.full_name = data.get('full_name')
        user.is_provider = data.get('is_provider')
        user.firebase_token = data.get('firebase_token')
        user.terms_conditions = data.get('terms_conditions')
        user.save()
        return user

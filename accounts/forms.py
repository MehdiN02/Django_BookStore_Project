from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):  # sakht form baraye sakhtan karbare jadid       hamishe hast
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'email']
        # fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):  # saskht form baraye taghire karbar       hanishe hast
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'email']

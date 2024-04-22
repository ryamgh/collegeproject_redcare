from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser,RequestBlood

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]



class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email Address'}))
    full_name = forms.CharField(label="Full Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Full Name'}))
    blood_group = forms.CharField(label="Blood Group", max_length=3, widget=forms.Select(choices=BLOOD_GROUP_CHOICES, attrs={'class':'form-control'}))
    gender = forms.CharField(label="Gender", max_length=1, widget=forms.Select(choices=GENDER_CHOICES, attrs={'class':'form-control'}))
    address = forms.CharField(label="Address", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your address'}))
    phone = forms.CharField(label="Phone Number", max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Phone Number'}))
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Date of Birth', 'type': 'date'}))  

    class Meta:
        model = CustomUser
        fields = ('full_name','username', 'email','phone',  'blood_group', 'gender', 'address', 'date_of_birth','image', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.blood_group = self.cleaned_data['blood_group']
        user.gender = self.cleaned_data['gender']
        user.address = self.cleaned_data['address']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        if commit:
            user.save()
        return user


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
# forms.py

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password')


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name', 'blood_group', 'gender', 'address','phone', 'date_of_birth','image']

# forms.py


class RequestBloodForm(forms.ModelForm):
    class Meta:
        model = RequestBlood
        fields = ['phone', 'city', 'address', 'blood_group', 'date']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}, choices=BLOOD_GROUP_CHOICES),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



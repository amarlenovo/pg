from django import forms
from django.contrib.auth.models import User
from django.core import validators
from pg.models import UploadPG,Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['user','profile_pic']

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        widgets={
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last Name'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}),
        }
    def clean(self):
        print("total Form Validation")
        cleaned_data=super().clean()
        pd1=cleaned_data['password']
        if len(pd1)<8:
            print('password must be 8 atleast charactters')
            raise forms.ValidationError('password must be atleast of 8 characters')

class UploadForm(forms.ModelForm):
    class Meta:
        model=UploadPG
        fields=['location','pgname','pgtype','pglocation','pgdescription','pgprice','pgcondition','pgmeals','ownername','pgmobile','ammenities1','ammenities2','ammenities3','ammenities4','ammenities5','ammenities6','ammenities7','ammenities8','ammenities9','ammenities10','pgimage1','pgimage2','pgimage3']

        widgets={
        'location':forms.Select(attrs={'class':'form-control'}),
        'pgname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PG/FLAT Name'}),
        'pgtype':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PG/FLAT Type'}),
        'pglocation':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PG/FLAT Location'}),
        'pgdescription':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PG/Flat Description'}),
        'pgprice':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PG/FLAT Price'}),
        'pgcondition':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PG/FLAT Condition'}),
        'pgmeals':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Meals Included or Not'}),
        'ownername':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Owner Name'}),
        'pgmobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Mobile'}),
        'ammenities1':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Ammenities'}),
        'ammenities2':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter second Ammenities'}),
        'ammenities3':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Third Ammenities'}),
        'ammenities4':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Fourth Ammenities'}),
        'ammenities5':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Fifth Ammenities'}),
        'ammenities6':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Sixth  Ammenities'}),
        'ammenities7':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Seventg Ammenities'}),
        'ammenities8':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Eighth Ammenities'}),
        'ammenities9':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Ninth Ammenities'}),
        'ammenities10':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Tenth Ammenities'}),
        'pgimage1':forms.FileInput(attrs={'class':'form-control'}),
        'pgimage2':forms.FileInput(attrs={'class':'form-control'}),
        'pgimage3':forms.FileInput(attrs={'class':'form-control'}),
        }

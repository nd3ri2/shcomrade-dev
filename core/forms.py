from django import forms
from .models import Registration
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class Login(forms.Form):
    member_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'p-2 rounded-md mx-auto'}))

    class Meta:
        widgets = {
            'member_number': forms.TextInput(attrs={'class': 'p-2 bg-slate-400 rounded-md mx-auto', 'placeholder': 'John'}),
        }

    def clean_all(self):
        member_no = self.cleaned_data['member_number']
        # validate age
        return member_no

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'member_number',
            'password',
            Submit('submit', 'Submit', css_class='bg-black rounded-md border text-white border-black px-5 text-end py-2 my-2 hover:bg-white hover:text-black')
        )


class Transaction(forms.Form):
    member_number = forms.CharField()
    phone_number = forms.CharField()
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'p-2 rounded-md mx-auto', 'min': 1000}))

    class Meta:
        widgets = {
            'member_number': forms.TextInput(attrs={'class': 'p-2 bg-slate-400 rounded-md mx-auto', 'placeholder': 'John'}),
            'phone_number': forms.NumberInput(attrs={'class': 'p-2 bg-slate-400 rounded-md mx-auto', 'placeholder':'254700000000', 'min': '254100000000'})
        ,}

    def clean_all(self):
        phone_no = self.cleaned_data['phone_number']
        # validate age
        return phone_no

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'member_number',
            'phone_number',
            'amount',
            Submit('submit', 'Submit', css_class='bg-black rounded-md border text-white border-black px-5 text-end py-2 my-2 hover:bg-white hover:text-black')
        )


class Leaver(forms.Form):
    member_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'p-2 rounded-md mx-auto'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'p-2 rounded-md mx-auto'}))

    def clean_all(self):
        password = self.cleaned_data['password']
        # validate age
        return password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'member_number'
            'password',
            Submit('submit', 'Submit', css_class='bg-black rounded-md border text-white border-black px-5 text-end py-2 my-2 hover:bg-white hover:text-black')
        )


class Register(forms.ModelForm):
    
    class Meta:
        model = Registration
        fields = ('first_name', 'second_name', 'date_of_birth', 'email', 'phone_number')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'p-2 rounded-md mx-auto', 'placeholder': 'John'}),
            'second_name': forms.TextInput(attrs={'class': 'p-2 rounded-md mx-auto', 'placeholder': 'Doe'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'p-2 rounded-md  mx-auto'}),
            'email': forms.EmailInput(attrs={'class': 'p-2 rounded-md  mx-auto', 'placeholder': 'johndoe@gmail.com'}),
            'phone_number': forms.NumberInput(attrs={})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'first_name',
            'second_name',
            'date_of_birth', 
            'email', 
            'phone_number',
            Submit('submit', 'Submit', css_class='bg-black rounded-md border text-white border-black px-5 text-end py-2 my-2 hover:bg-white hover:text-black')
        )



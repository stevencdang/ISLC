from django import forms
from website.models import Registration


class RegistrationForm(forms.ModelForm):
    email_confirm = forms.CharField(max_length=254)

    class Meta:
        model = Registration
        fields = ['first_name',
                  'last_name',
                  'email',
                  'email_confirm',
                  'phone',
                  'status',
                  'slc',
                  'department',
                  'university',
                  'research',
                  'nr1',
                  'nr2',
                  'nr3',
                  'diet',
                  'special_needs']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'text',
                                                       'name': 'first_name',
                                                       'placeholder': 'First',
                                                       'type': 'text',
                                                       'value': ''})
        self.fields['last_name'].widget.attrs.update({'class': 'text',
                                                       'name': 'last_name',
                                                       'placeholder': 'Last',
                                                       'type': 'text',
                                                       'value': ''})
        self.fields['email'].widget.attrs.update({'class': 'text',
                                                  'name': 'email',
                                                  'placeholder': 'Email',
                                                  'type': 'email',
                                                  'value': ''})
        self.fields['email_confirm'].widget.attrs.update({'class': 'text',
                                                          'name': 'email_verify',
                                                          'placeholder': 'Verify Email',
                                                          'type': 'email',
                                                          'value': ''})
        self.fields['status'].widget.attrs.update({'class': 'text',
                                                   'name': 'student_status'})
        self.fields['slc'].widget.attrs.update({'class': 'text',
                                                'name': 'center'})
        self.fields['department'].widget.attrs.update({'class': 'text',
                                                       'name': 'department',
                                                       'placeholder': 'Department',
                                                       'type': 'text',
                                                       'value': ''})
        self.fields['university'].widget.attrs.update({'class': 'text',
                                                       'name': 'university',
                                                       'placeholder': 'University',
                                                       'type': 'text',
                                                       'value': ''})
        self.fields['research'].widget.attrs.update({'class': 'value',
                                                     'name': 'research_interests'})
        self.fields['nr1'].widget.attrs.update({'class': 'text',
                                                'name': 'nonresearch_interest_first'})
        self.fields['nr2'].widget.attrs.update({'class': 'text',
                                                'name': 'nonresearch_interest_second'})
        self.fields['nr3'].widget.attrs.update({'class': 'text',
                                                'name': 'nonresearch_interest_third'})
        self.fields['diet'].widget.attrs.update({'class': 'text',
                                                 'name': 'diet'})
        self.fields['special_needs'].widget.attrs.update({'class': 'text',
                                                   'name': 'special_needs'})

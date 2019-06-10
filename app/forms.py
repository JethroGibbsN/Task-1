from django import forms
PLAN_CHOICES=[
	('plan1', 'Plan1'),
	('plan2', 'Plan2'),
	('plan3', 'Plan3')
]
class SignupForm(forms.Form):
	name = forms.CharField(label='Enter your name', max_length=100)
	email = forms.EmailField(label='Enter your email', max_length=100)
	plan_choices=forms.CharField(label='Select a plan',widget=forms.Select(choices=PLAN_CHOICES))
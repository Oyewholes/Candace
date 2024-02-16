from django import forms  
from .models import Comment, Subscriber
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields= ['name', 'body']
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Submit', css_class='bg-blue-500 hover:bg-blue-700 text-black font-bold py-2 px-4 rounded'))
    
class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
          'email':forms.EmailInput(attrs={'placeholder': 'Enter email address'})
        }
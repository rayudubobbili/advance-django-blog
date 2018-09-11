from django import forms
from .models import Comments


class ContactForm(forms.Form):
    # TODO: Send the email to register user with the form data
    name = forms.CharField(
            max_length=100,
            required=True,
            )
    email = forms.EmailField(
            required=True,
            )
    subject = forms.CharField(
            max_length=300,
            required=True,
           )
    message = forms.CharField(
            max_length=2000,
            widget=forms.Textarea(),
           help_text="write your message")

    def clear(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidateionError("Need to write something!")


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('name', 'email', 'comment')

    def clear():
        cleaned_data = super(CommentsForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        comment = cleaned_data.get('comment')


class PostSearchForm(forms.Form):
    post_name = forms.CharField(max_length=200)

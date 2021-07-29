
from django import forms
from .models import *
from .mixins import *

# brands
class BrandForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Brand
        fields = "__all__"

# cars
class CarForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Car
        fields = "__all__"
        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['is_on_sale'].widget.attrs.update({
              'class': "control outlined control-checkbox checkbox-success"
          })
          self.fields['is_on_rent'].widget.attrs.update({
              'class': "control outlined control-checkbox checkbox-success"
          })
          self.fields['is_featured'].widget.attrs.update({
              'class': "control outlined control-checkbox checkbox-success"
          })
          self.fields['brand'].widget.attrs.update({
              'class': 'form-control select2'
          })
          self.fields['model'].widget.attrs.update({
              'class': 'form-control select2'
          })
          self.fields['type'].widget.attrs.update({
              'class': 'form-control select2'
          })
          self.fields['category'].widget.attrs.update({
              'class': 'form-control select2'
          })
          self.fields['features'].widget.attrs.update({
            'class': 'form-control select2 feature-select',
            'multiple': 'multiple'
          })

# carimage
class CarImageForm(forms.ModelForm):
  class Meta:
    model = CarImage
    fields = '__all__'


# models
class ModelForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Model
        fields = "__all__"


# types
class TypeForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Type
        fields = "__all__"


# categories
class CategoryForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Category
        fields = "__all__"

# features
class FeatureForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Features
        fields = "__all__"


# about
class AboutForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = About
        fields = "__all__"
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            })
        }

# team
class TeamForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Team
        fields = "__all__"
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            })
        }

# services
class ServicesForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Services
        fields = "__all__"
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            })
        }

# services-video
class ServicesVideoForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = ServicesVideo
        fields = "__all__"

# services-video
class ContactForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Contact
        fields = "__all__"
       
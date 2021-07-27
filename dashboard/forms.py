
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

# models
class ModelForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Model
        fields = "__all__"




from django import forms
from .models import *
from .mixins import *

# brands
class BrandForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Brand
        fields = "__all__"

# cars
class BrandForm(FormControlMixin, forms.ModelForm):
      class Meta:
        model = Car
        fields = "__all__"

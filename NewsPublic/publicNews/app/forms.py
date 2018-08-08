from django import forms
from .models import MOU,Student
from django.utils.translation import gettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'expire_date'

class MOUForm(forms.ModelForm):
    class Meta:
        model = MOU
        fields = '__all__'
        widgets = {
            'start_date': DateInput(),
            'expire_date': DateInput(),
        }
        labels  = {
            "title" : _("ชื่อเรื่อง"),
            "start_date" : _("เริ่มวันที่"),
            "expire_date" : _("สิ้นสุดวันที่"),
            "tpye" : _("ประเภท"),
            "contact" : _("ติดต่อ"),
            "url" : _("เอกสารแนบ"),
        }
        

class StudentForm(forms.ModelForm):
    class Meta:
        model =  Student
        exclude=[]
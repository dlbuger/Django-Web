from django import forms

class EmployeeRecord(forms.Form):
    姓名 = forms.CharField(widget=forms.TextInput(), required=True)
    员工号 = forms.CharField(widget=forms.TextInput(), required=True)
    部门 = forms.CharField(widget=forms.TextInput())
    单位人工 = forms.FloatField(widget=forms.TextInput())
    预算人工 = forms.FloatField(widget=forms.TextInput())
    实际人工 = forms.FloatField(widget=forms.TextInput())

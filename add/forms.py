from django import forms
from datetime import datetime

def get_today():
    return datetime.now().date()

def get_yesterday():
    return datetime.now().date()

TODAY = get_today
YESTERDAY = get_yesterday

DATE_SELECTION = (
    (TODAY, "今天"),
    (YESTERDAY, "昨天")
)


class ProgramRecord(forms.Form):
    # 项目名称
    项目名称 = forms.CharField(widget=forms.TextInput(), required=True)
    
    # 合同号
    合同号 = forms.CharField(widget=forms.TextInput(), required=True)
    
    # 开始时间
    计划开始时间 = forms.DateField(required=False)
    实际开始时间 = forms.DateField(required=False)
    
    # 结束时间
    计划结束时间 = forms.DateField(required=False)
    实际结束时间 = forms.DateField(required=False)
    
    # 硬件成本
    计划硬件成本 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'type':'date'}))
    实际硬件成本 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'type':'date'}))
    
    # 软件成本
    计划软件成本 = forms.FloatField(required=False,  widget=forms.TextInput(attrs={'type':'date'}))
    实际软件成本 = forms.FloatField(required=False,  widget=forms.TextInput(attrs={'type':'date'}))

    # 施工成本
    计划施工成本 = forms.FloatField(required=False,  widget=forms.TextInput(attrs={'type':'date'}))
    实际施工成本 = forms.FloatField(required=False,  widget=forms.TextInput(attrs={'type':'date'}))

    # 差旅成本
    计划差旅成本 = forms.FloatField(required=False,  widget=forms.TextInput(attrs={'type':'date'}))
    实际差旅成本 = forms.FloatField(required=False,  widget=forms.TextInput(attrs={'type':'date'}))

    # 集成成本
    计划集成成本 = forms.FloatField(required=False,  widget=forms.TextInput(attrs={'type':'date'}))
    实际集成成本 = forms.FloatField(required=False,  widget=forms.TextInput(attrs={'type':'date'}))


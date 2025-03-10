from django import forms
from .models import ContractTemplate, ContractInstance

class ContractTemplateForm(forms.ModelForm):
    class Meta:
        model = ContractTemplate
        fields = ['name', 'template_file']

class ContractInstanceForm(forms.ModelForm):
    class Meta:
        model = ContractInstance
        fields = []

    def __init__(self, *args, **kwargs):
        contract_template = kwargs.pop('contract_template', None)
        super().__init__(*args, **kwargs)
        if contract_template:
            for variable in contract_template.variables:
                self.fields[variable] = forms.CharField(label=variable)

class SendContractForm(forms.Form):
    recipient_email = forms.EmailField()

from django.db import models
from docx import Document
import re
from collections import OrderedDict

class ContractTemplate(models.Model):
    name = models.CharField(max_length=100)
    template_file = models.FileField(upload_to='templates/')
    created_at = models.DateTimeField(auto_now_add=True)
    variables = models.JSONField(editable=False, default=list)

    def __str__(self):
        return self.name

    def extract_variables(self):
        # Ensure the file is saved before reading it
        self.template_file.open()
        doc = Document(self.template_file)
        variables = OrderedDict()
        variable_pattern = re.compile(r'<<%\s*(\w+)\s*%>>')
        
        for paragraph in doc.paragraphs:
            matches = variable_pattern.findall(paragraph.text)
            for match in matches:
                variables[match] = None  # Use None as a placeholder value
        
        self.template_file.close()
        return list(variables.keys())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first to ensure the file is available
        if not self.variables:  # Only extract variables if not already set
            self.variables = self.extract_variables()
            super().save(update_fields=['variables'])

class ContractInstance(models.Model):
    template = models.ForeignKey(ContractTemplate, on_delete=models.CASCADE)
    variables = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Instance of {self.template.name}"

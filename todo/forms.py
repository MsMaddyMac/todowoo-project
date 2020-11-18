from django.forms import ModelForm
from .models import Todo

# This will use a Django ModelForm based on the Todo model we created
class TodoForm(ModelForm):
  class Meta:
    # Uses the model imported on line 2 above (Todo)
    model = Todo
    # Will create fields based on the model fields passed in the list below
    fields = ['title', 'memo', 'important']
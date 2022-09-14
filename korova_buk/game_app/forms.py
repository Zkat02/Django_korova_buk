from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import re

from game_app.models import BaseWords

class UserInputWordForm(forms.Form):
     word = forms.CharField(max_length=4,label="слово",widget=forms.TextInput(attrs={"class":"form-control"}))

     def clean_word(self):
          word = self.cleaned_data['word']
          word = word.lower()

          if re.match('\d', word):  # если названия начинается с цифры
              raise ValidationError('слово не должно начинаться с цифры')
          else:
               try:
                    BaseWords.objects.get(base_word=word)
                    return word
               except ObjectDoesNotExist:
                    raise ValidationError('мне очень жаль, но я не знаю такого слова :(')


import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text=_('form.renew_book.renewal_date.help_text'))

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('form.renew_book.renewal_date.invalid.in_past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('form.renew_book.renewal_date.invalid.too_far_in_future'))

        return data

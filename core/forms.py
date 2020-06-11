from django import forms

PAG_CHOISES = {
    ('1',1),
    ('5',5),
    ('10',10),
    ('25',25),
    ('50',50)
}

class PagForm(forms.Form):
    pag_by = forms.IntegerField(label='מספר מוצרים בעמוד',
                                widget=forms.Select(choices=PAG_CHOISES,
                                                    attrs={'dir': 'rtl',
                                                           'class':'pag_ch'}),
                                required=True)
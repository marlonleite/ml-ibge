from django import forms

from ml_ibge.ibge import IBGE


class MLIBGEMixinForm(forms.ModelForm):
    state = forms.ChoiceField(label="Estado")
    city = forms.ChoiceField(label="Cidade")

    def __init__(self, *args, **kwargs):
        super(MLIBGEMixinForm, self).__init__(*args, **kwargs)
        default_choices = [("", "Escolha uma opção")]
        self.fields["state"].choices = default_choices + self._choices_states()
        self.fields["city"].choices = []

        if "state" in self.data:
            state = self.data.get("state")
            self.fields["city"].choices = default_choices + self._choices_cities(state)
        elif self.instance.pk:
            self.fields["city"].choices = default_choices + self._choices_cities(
                self.instance.state
            )
            self.initial["city"] = self.instance.city

    def _choices_states(self):
        return [(state["UF-sigla"], state["UF-nome"]) for state in IBGE.get_states()]

    def _choices_cities(self, uf):
        return [
            (city["distrito-nome"], city["distrito-nome"])
            for city in IBGE.get_cities(uf)
        ]

=====
ML IBGE
=====

Quick start
-----------

1. Add "ml_ibge" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ml_ibge',
    ]

2. Add in the "admin.py" file the fallow code:

    @admin.register(Example)
    class ExampleAdmin(MLIBGEMixinAdmin):
        form = ExampleAdminForm
        change_form_template = "admin/example/example_change_form.html"


3. Add in the "example_change_form.html" file the fallow javascript code:

    {% extends "admin/change_form.html" %}

    {% block admin_change_form_document_ready %}{{ block.super }}
        {% include "ml_ibge/admin/change_form_script.html" %}
    {% endblock %}

4. Add in the "forms.py" file the fallow code:

    class ExampleAdminForm(MLIBGEMixinForm):
        class Meta:
            ...
            fields = (... "state", "city", ...)
            ...

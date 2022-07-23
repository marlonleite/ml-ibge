from django.contrib import admin, messages
from django.shortcuts import render
from django.urls import path

from ml_ibge.ibge import IBGE


class MLIBGEChangeFormTemplateNotFound(Exception):
    pass


class MLIBGEMixinAdmin(admin.ModelAdmin):

    def get_changelist(self, request, **kwargs):
        try:
            if self.change_form_template is None:
                raise MLIBGEChangeFormTemplateNotFound("ML IBGE ChangeFormTemplate not found!")
        except MLIBGEChangeFormTemplateNotFound as exc:
            self.message_user(request, exc, level=messages.WARNING)
        return super(MLIBGEMixinAdmin, self).get_changelist(request, **kwargs)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("admin/select/cities/options", self._get_cities_options, name="select_cities"),
        ]
        return my_urls + urls

    def _get_cities_options(self, request):
        context = {}
        state = request.GET.get("state")
        if state:
            context["cities"] = [city["distrito-nome"] for city in IBGE.get_cities(state)]
        return render(request, "ml_ibge/admin/cities_options.html", context)

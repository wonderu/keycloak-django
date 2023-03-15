# -*- coding: utf-8 -*-
from django.conf import settings
from allauth.socialaccount.providers.keycloak.provider import KeycloakProvider


OVERRIDE_NAME = (
    getattr(settings, "SOCIALACCOUNT_PROVIDERS", {})
    .get("customkeycloak", {})
    .get("OVERRIDE_NAME", "CustomKeycloak")
)

class CustomKeycloakProvider(KeycloakProvider):
    id = "customkeycloak"
    name = OVERRIDE_NAME

    def sociallogin_from_response(self, request, response):
        social_login = super().sociallogin_from_response(request, response)
        extra_data = self.extract_extra_data(response)
        print(extra_data)
        return social_login

provider_classes = [CustomKeycloakProvider]

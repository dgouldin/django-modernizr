from django.conf import settings

def contribute_to_settings(defaults):
    for attr, value in defaults.items():
        if not hasattr(settings, attr):
            setattr(settings, attr, value)

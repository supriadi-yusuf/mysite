import django.dispatch

supri_signal = django.dispatch.Signal(providing_args=['name','age'])

def get_supri_signal():
    return supri_signal

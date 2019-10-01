from django.dispatch import receiver
from .signals import get_supri_signal

# register function 'watch_4_signal' as receiver of signal returned by get_supri_signal() function
@receiver(get_supri_signal())
def watch_4_signal( sender, name, age, **kwargs):
    print('supri_signal is received name : %s, age : %d' % (name, age))

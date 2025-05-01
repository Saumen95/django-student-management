from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from .models import ActivityLog

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ActivityLog.objects.create(user=user, action_type='LOGIN', status='SUCCESS')

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ActivityLog.objects.create(user=user,
                               action_type='LOGOUT',
                               status='SUCCESS')

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    ActivityLog.objects.create(user=None,
                               action_type='LOGIN_FAILED',
                               status='FAILED',
                               remarks=credentials.get('username'))

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.db.models.signals import post_save
from django.core.mail import send_mail, EmailMessage
from rest_framework.authtoken.models import Token
from customers.models import Customer




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
    email_plaintext_message = "Open the link to reset your password" + " " + "{}{}".format(instance.request.build_absolute_uri("https://videoflix.claudia-daneder.com/reset-password-form/"), reset_password_token.key)

    """
        this below line is the django default sending email function,
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        # title:
        "Password reset for your Videoflix account",
        # message:
        email_plaintext_message,
        # from:
        "videoflix@claudia-daneder.com",
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )

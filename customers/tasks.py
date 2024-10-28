from django.core.mail import send_mail


def send_activation_email(customer):
    activation_link = f"https://videoflix.claudia-daneder.com/activate/{customer.activation_token}/"
    subject = 'Activate your account'
    message = f'Please click the following link to activate your account: {activation_link}'
    send_mail(subject, message, 'videoflix@claudia-daneder.com', [customer.email])

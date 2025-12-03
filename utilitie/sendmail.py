from django.core.mail import EmailMultiAlternatives


def SendMail(subject, html_content):
    from_email = "hassanrakibul926@gmail.com"
    to_email = ["wawireb139@bialode.com"]
    
    email = EmailMultiAlternatives(subject, "", from_email, to_email)
    email.attach_alternative(html_content, 'text/html')
    email.send()
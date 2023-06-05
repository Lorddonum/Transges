from django.test import TestCase
from django.core.mail import send_mail


# Create your tests here.

class TestEmails(TestCase):
    def test_emails(self):
        subject = "TEST!",
        message = "IZUMI IS TESTING THIS SO THERE YOU GO!",
        from_email = "khatbane.atae@gmail.com",
        recipient_list = ["635shadows@gmail.com"],
        fail_silently=False,
        auth_user="khatbane.atae@gmail.com",
        auth_password="@Alpha321-",
        result = send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password )
        print("result =>", result)
from ..common import *
config.load('smtp', globals())

# SMTP related
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
provide email function
"""

__all__ = [ 'sendmail' ]

def sendmail(receiver, subject, content_html=None, content_text=None):
    """
    send email to reciver(s) with subject and html or plaintext content.
    either `content_html` or `content_text` must be assigned, or in both.

    :param receiver: receivers' email address, could be str or list of str
    :param subject: subject
    :param content_html: content in html format
    :param content_text: content in plain text
    :type receiver: str, list
    :type subject: str
    :type content_html: str
    :type content_text: str
    """
    if not content_text and not content_html:
        raise ValueError('either `content_html` or `content_text` must be set')

    message = MIMEMultipart()
    message['From'] = SMTP_FROM
    message['To'] = receiver  # TODO: how to send multi-receiver mail?
    message['Subject'] = subject

    if content_html:
        message.attach(MIMEText(content_html, 'html'))
    if content_text:
        message.attach(MIMEText(content_text, 'plain'))

    smtp_client = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    if SMTP_USE_TLS:
        smtp_client.starttls()
    smtp_client.login(SMTP_USER, SMTP_PASSWORD)
    retvalue = smtp_client.sendmail(SMTP_FROM, receiver, message.as_string())
    smtp_client.quit()
    return retvalue

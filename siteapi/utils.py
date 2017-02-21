import re


# --------------------------------------------------------------------------------------------------
# File Constants

email_regex = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{'
                         r'1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{'
                         r'2,}))$')
writer_regex = re.compile(r'^([A-Za-z][0-9A-Za-z_\- ]+)$')


def match_email_rgx(email):
    return email_regex.search(email) is not None


def match_writer_rgx(writer):
    return writer_regex.search(writer) is not None


def make_error(error, extra=None):
    if extra:
        return dict(id='failure', data=dict(message=error, extra=extra))
    return dict(id='failure', data=dict(message=error))

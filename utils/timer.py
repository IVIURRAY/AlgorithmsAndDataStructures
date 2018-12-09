import datetime


class Timer(object):
    """Context manager to time duration of algorithms"""

    def __init__(self):
        self.start = datetime.datetime.now()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = datetime.datetime.now()
        duration = end - self.start
        print('\n Timer info: \n Seconds: %s \n Microseconds: %s \n' % (duration.seconds, duration.microseconds))


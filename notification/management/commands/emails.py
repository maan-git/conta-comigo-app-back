import abc


class Emails(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def mount_email(self, email):
        return

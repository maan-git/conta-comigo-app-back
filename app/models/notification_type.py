from utils.simple_description_base import SimpleDescriptionBaseWithId


class NotificationType(SimpleDescriptionBaseWithId):
    class AllTypes:
        USER_APPLIED_TO_HELP = 1
        USER_UNAPPLIED_FROM_HELP = 2

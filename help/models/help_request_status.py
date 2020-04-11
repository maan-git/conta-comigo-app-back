from utils.simple_description_base import SimpleDescriptionBaseWithId


class HelpRequestStatus(SimpleDescriptionBaseWithId):
    class AllStatus:
        Created = 1
        InProgress = 20
        Canceled = 99
        Finished = 100

from datetime import datetime


class PostModel(object):
    id: int
    created: datetime
    title: str
    content: str

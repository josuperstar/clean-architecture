from datetime import datetime


class Post(object):
    id: int
    created: datetime
    title: str
    content: str

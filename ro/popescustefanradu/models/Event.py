from sqlite3.dbapi2 import Date


class Event(object):
    def __init__(self, date: Date, title: str, text: str, short_text: str):
        self.date, self.title, self.test, self.short_text = date, title, text, short_text

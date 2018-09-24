from google.appengine.ext import ndb


class Book(ndb.Model):
    'to describe a book class'
    BCode = ndb.IntegerProperty(required=True)
    BTitle = ndb.StringProperty()
    BPrice = ndb.FloatProperty()
    BPages = ndb.IntegerProperty()
    BPub   = ndb.StringProperty()
    BDesc = ndb.StringProperty()



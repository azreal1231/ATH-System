from couchdb.mapping import *


class vehicle(Document):
    REGISTRATION_PLATE = TextField(default='')

    lAST_USERS = TextField(default='')

    CURRENT_USERS = TextField(default='')

    VE = DictField(default={'': {'Amount': ''}, '': {'Amount': ''}})

    MSE = DictField(default={'': {'Amount': ''}, '': {'Amount': ''}})

    PPE = DictField(default={'': {'Amount': ''}, '': {'Amount': ''}})

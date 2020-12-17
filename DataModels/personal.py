from couchdb.mapping import *


class Personal(Document):
    ID_Number = TextField(default="")
    Name = TextField(default="")
    Surname = TextField(default="")
    Contact_Details = DictField(default={'Contact_Number': '', 'Contact_Email': ''})
    Emergency_Contact_Details = DictField(default={'Contact_Number': '', 'Contact_Email': ''})
    Age = TextField(default="")
    Marital_Status = ListField(default=["Single", "Married", "In Relationship"])

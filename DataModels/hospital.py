from couchdb.mapping import *


class Hospital(Document):
    Location = DictField(default={'Physical_Address': '', 'Plus_Code': ''})
    Contact_Details = DictField(default={'Contact_Number': '', 'Contact_Email': '', 'ICU_Num': ''})
    NOB = TextField(default='')
    Wards = DictField(default={'Pediatrics': {'NOB': ''}, 'Maternity': {'NOB': ''}, 'Geriatrics': {'NOB': ''},
                               'Psychiatric': {'NOB': ''}})
    Workers = DictField(default={'Specialists': '', 'Registered_Nurses': '', 'Licensed_Practical_Nurses': '',
                                 'Patient_Advocate': '', 'Patient_Care_Technicians': '', 'Physical_Therapists': '',
                                 'Occupational therapists': '', 'Hospital pharmacists': '',
                                 'Social_Workers': '', 'Dietitians': '',
                                 'Interpreter_Services': '', 'Rapid_Response_Team': ''})

from app import db

class Feed_Name(db.Model):
    Feed_Name = Column(VARCHAR(256), primary_key = True)
    Carrier_Id = Column(VARCHAR(64))
    Employer_Ids = Column(VARCHAR(256))
    Vendor_Tax_Id = Column(VARCHAR(256))
    File_Is_3030 = Column(Boolean, default = 0)
    

    def __repr__(self):
        return '<Post %r>' % (self.body)

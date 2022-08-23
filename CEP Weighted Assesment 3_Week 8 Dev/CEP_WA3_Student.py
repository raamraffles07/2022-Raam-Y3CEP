class Student:

    def __init__(self, offencelist = [], badgelist = [], brokenitems = []):
        self.offencelist = offencelist
        self.badgelist = badgelist
        self.brokenitems = brokenitems

    ###Boring Student Details

    def set_name(self, name):
        self.name = name

    def set_identification(self, classs):
        self.classs = classs

    def reg_num(self, reg_num):
        self.reg_num = reg_num
    
    def batchnum(self, batchnum):
        self.batchnum = batchnum
    
    def set_numoffences(self, num_of_offences):
        self.num_of_offences = num_of_offences
    
    def set_numbadges(self, number_of_badges):
        self.number_of_badges = number_of_badges
        
    def set_numbrokeni(self, number_of_bi):
        self.number_of_brokenitems = number_of_bi
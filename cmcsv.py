
import os
import csv
import datetime
import pytz



def record_log(self, details=""):

    os.chdir(os.path.expanduser("~/Desktop"))     # r means the string will be treated as raw string
                                                                    # r"C:\a\foo"
                                                                    #  "C:/a/foo"
    with open(f"log{self.id}.csv", "a", newline='') as csv_file:    #add newline='' in order to eliminate linebreak for every written line

        fieldname = ["first", "last", "id", "type", "details", "balance", "datetime"]   
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname, delimiter="-")

        if self.header_switch:
            csv_writer.writeheader()    #write a header based on info in fieldname
            self.header_switch = False  #makes the header of csv show up only once

        csv_writer.writerow({"first":self.first, "last":self.last, "id":self.id, "type":self.log_type, "details":details,       #record log
            "balance": self.balance, "datetime":datetime.datetime.now(tz=pytz.timezone("UTC"))})        #datetime is in UTC
        


import csv
with open("records.txt","w") as csvfile:
    header=['ID','NAME','AGE','FACULTY']
    data=[[1,'Ram',20,'BIM'],
          [2,'Hari',21,'BIM'],
          [3,'Shyam',20,'BCA']]
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)
    csvfile.close()
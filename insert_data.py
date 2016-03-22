__author__ = 'Pymaverics'
#import required libraries
import csv
import pymongo

connection = pymongo.MongoClient("mongodb://pymavericks:Nbeke44H@labs.ayokasystems.com/?authSource=pymavericks")

db = connection.pymavericks
file_path = "D:\\Pymaverics\\"

# function to read csv/flat files
def readdata(filename,delimiter):
    file_content = []
    rec_id = 0
    final_data = {}
    with open(file_path + filename )as demo:
        data = csv.reader(demo,delimiter = delimiter)
        for lines in data:
            file_content.append(lines)
    data_slice = file_content[1:len(file_content)]

    for row in data_slice:
        rec_id = rec_id + 1
        merge_dict = {}
        for index in range(0,len(file_content[0]),1):

            merge_dict.update({file_content[0][index]:row[index]})
            print file_content[0][index],row[index]

        final_data.update({rec_id:merge_dict})

    return final_data

# call the read data function with appropriate filename and delimiters
indi_data = readdata("INDI13Q4.txt","$")
#insert data into indi_data collection
for k,v in indi_data.items():
        db.indi_data.insert(v)

demo_data = readdata("DEMO13Q4.txt","$")
#insert data into demo_data collection
for k,v in demo_data.items():
        db.demo_data.insert(v)


drug_data = readdata("DRUG13Q4.txt","$")
#insert data into drug_data collection
for k,v in drug_data.items():
        db.drug_data.insert(v)

ndfrt_public_data = readdata("NDFRT_Public_2014.07.07_NUI.txt","\t")
#insert data into ndfrt_public_data collection
for k,v in ndfrt_public_data.items():
        db.ndfrt_public_data.insert(v)

outc_data = readdata("OUTC13Q4.txt","$")
#insert data into outc_data collection
for k,v in outc_data.items():
        db.outc_data.insert(v)

reac_data = readdata("REAC13Q4.txt","$")
#insert data into reac_data collection
for k,v in reac_data.items():
        db.reac_data.insert(v)

rpsr_data = readdata("RPSR13Q4.txt","$")
#insert data into rspsr_data collection
for k,v in rpsr_data.items():
        db.rpsr_data.insert(v)

rxterms_data = readdata("RxTerms201408.txt","|")
#insert data into rxterms_data collection
for k,v in rxterms_data.items():
        db.rxterms_data.insert(v)

rxarch_data = readdata("RxTermsArchive201408.txt","|")
#insert data into rxarch_data collection
for k,v in rxarch_data.items():
        db.rxarch_data.insert(v)

rxingr_data = readdata("RxTermsIngredients201408.txt","|")
#insert data into rxingr_data collection
for k,v in rxingr_data.items():
        db.rxingr_data.insert(v)

ther_data = readdata("THER13Q4.txt","$")
#insert data into rxingr_data collection
for k,v in ther_data.items():
        db.ther_data.insert(v)




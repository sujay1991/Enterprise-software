__author__ = 'Pymaverics'
import csv
import xml.etree.ElementTree as ET

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

        final_data.update({rec_id:merge_dict})




    return final_data

#function to read xml file
def readxml(filename):
    tree = ET.parse(file_path + filename)
    root = tree.getroot()
    return tree,root

# call the read data function with appropriate filename and delimiters
indi_data = readdata("INDI13Q4.txt","$")
demo_data = readdata("DEMO13Q4.txt","$")
drug_data = readdata("DRUG13Q4.txt","$")
ndfrt_data = readdata("NDFRT_Public_2014.07.07_NUI.txt","\t")
outcome_data = readdata("OUTC13Q4.txt","$")
reac_data = readdata("REAC13Q4.txt","$")
rpsr_data = readdata("RPSR13Q4.txt","$")
rxterms_data = readdata("RxTerms201408.txt","|")
rxarch_data = readdata("RxTermsArchive201408.txt","|")
rxingr_data = readdata("RxTermsIngredients201408.txt","|")
ther_data = readdata("THER13Q4.txt","$")

#call the readxml function with the filename as input
ndfrt_tree,ndfrt_root = readxml("NDFRT_Public_2014.07.07_TDE.xml")








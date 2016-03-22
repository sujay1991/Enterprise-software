import pymongo
connection = pymongo.MongoClient("mongodb://pymavericks:Nbeke44H@labs.ayokasystems.com/?authSource=pymavericks")
db = connection.pymavericks
file_path = "D:\\Pymaverics\\"

#Open the temporary file populated in parse_xml 
f = open(file_path+"temp_out.txt")

doc = []
#populate the content of the file to a temporary dictionary.
for line in f:
			
	temp_list = []
	for word in line.split():
		temp_list.append(word)

	if temp_list[0] == "DefType":
		temp_dict = {}
		temp_dict[temp_list[0]] = temp_list[1]
		doc.append(temp_dict)

	else:
		temp_dict = {}
		l = len(doc)
		temp_dict[temp_list[0]] = " ".join(temp_list[1:])
		doc[l-1].update(temp_dict)

#Insert the data in the dictionary to the DB Collection
for items in doc:
	db.NDFRT_public.insert(items)

print "Data inserted"	


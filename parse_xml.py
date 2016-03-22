
import xml.sax
import sys
#temporary file's file_path refers to the local file path to store the content of XML after parsing.
file_path = "D:\\Pymaverics\\"
f_out=open(file_path+"temp_out.txt","w")
#Content handler class that serves as a template for the xml.
class DefHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.currentData = ""
		self.name = ""
		self.code = ""
		self.id = ""
		self.namespace = ""
		self.primitive = ""
		self.kind = ""
		self.concept = ""
		self.range = ""
		self.domain = ""
		self.inverseName = ""
		self.pickListItem = ""
		self.tagList = ["definingRoles","properties","qualifiers","pickList","root"]
		self.list1 = ["kindDef","qualifierDef"]
		self.list2 = ["propertyDef", "roleDef","namespaceDef","associationDef"]
		self.stack = []
		self.d_counter = 0
		self.pn_counter = 0
		self.pv_counter = 0
		self.qn_counter = 0
		self.qv_counter = 0
		self.pl_counter = 0
#function to parse the XML and write the attributes to temporary file. 
#Pushes tags to a stack for handling multiple tags with same name in same hierarchy level.
	def startElement(self, tag, attributes):
		self.currentData = tag
		self.stack.append(tag)
		if tag == "conceptDef":
			print "DefType", tag
			f_out.write("DefType")
			f_out.write(" ")
			f_out.write(tag)
			f_out.write("\n")
			self.d_counter = 1
			self.pn_counter = 1
			self.pv_counter = 1
			self.qn_counter = 1
			self.qv_counter = 1
		elif tag in self.list1:
			print "DefType", tag
			f_out.write("DefType")
			f_out.write(" ")
			f_out.write(tag)
			f_out.write("\n")
			for k,v in attributes.items():
				print k,"",v
				f_out.write(k)
				f_out.write("")
				f_out.write(v)
				f_out.write("\n")

			if tag == "qualifierDef":
				self.pl_counter = 1
		elif tag in self.list2:
			print "DefType",tag
			f_out.write("DefType")
			f_out.write(" ")
			f_out.write(tag)
			f_out.write("\n")
	#function to pop from the stack accordingly to the tag name and write to the file accordingly.
	def endElement(self, tag):
		if self.currentData in self.tagList:
			self.stack.pop()
		if self.currentData == "conceptDef":
			self.stack.pop()
		if self.currentData == "definingConcepts":
			self.stack.pop()
			self.d_counter = 1
		if self.currentData == "property":
			self.stack.pop()
			self.pn_counter = 1
			self.pv_counter = 1
		if self.currentData == "qualifier":
			self.stack.pop()
			self.qn_counter = 1
			self.qv_counter = 1
		if self.currentData == "namespace":
			self.stack.pop()
			print "namespace",self.namespace
			f_out.write("namespace")
			f_out.write(" ")
			f_out.write(self.namespace)
			f_out.write("\n")
		elif self.currentData == "code":
			self.stack.pop()
			print "code",self.code
			f_out.write("code")
			f_out.write(" ")
			f_out.write(self.code)
			f_out.write("\n")
		elif self.currentData == "id":
			self.stack.pop()
			print "id",self.id
			f_out.write("id")
			f_out.write(" ")
			f_out.write(self.id)
			f_out.write("\n")
		elif self.currentData == "primitive":
			self.stack.pop()
			print "primitive",self.primitive
			f_out.write("primitive")
			f_out.write(" ")
			f_out.write(self.primitive)
			f_out.write("\n")
		elif self.currentData == "kind":
			self.stack.pop()
			print "kind",self.kind
			f_out.write("kind")
			f_out.write(" ")
			f_out.write(self.kind)
			f_out.write("\n")
		elif self.currentData == "range":
			self.stack.pop()
			print "range", self.range
			f_out.write("range")
			f_out.write(" ")
			f_out.write(self.range)
			f_out.write("\n")
		elif self.currentData == "domain":
			self.stack.pop()
			print "domain", self.domain
			f_out.write("domain")
			f_out.write(" ")
			f_out.write(self.domain)
			f_out.write("\n")
		elif self.currentData == "inverseName":
			self.stack.pop()
			print "inverseName", self.inverseName
			f_out.write("inverseName")
			f_out.write(" ")
			f_out.write(self.inverseName)
			f_out.write("\n")
		elif self.currentData == "concept":
			self.stack.pop()
			if self.stack[-1] == "definingConcepts":
				print "definingConcept_" + str(self.d_counter),self.concept
				f_out.write("definingConcept_"+str(self.d_counter))
				f_out.write(" ")
				f_out.write(self.concept)
				f_out.write("\n")
				self.d_counter = self.d_counter + 1
		elif self.currentData == "name":
			self.stack.pop()
			if self.stack[-1] == "property":
				print "property_" + str(self.pn_counter) + "_name",self.name
				f_out.write("property_" + str(self.pn_counter) + "_name")
				f_out.write(" ")
				f_out.write(self.name)
				f_out.write("\n")
				self.pn_counter = self.pn_counter + 1
			elif self.stack[-1] == "qualifier":
				print "qualifier_" + str(self.qn_counter) + "_name",self.name
				f_out.write("qualifier_" + str(self.qn_counter) + "_name")
				f_out.write(" ")
				f_out.write(self.name)
				f_out.write("\n")
				self.qn_counter = self.qn_counter + 1
		elif self.currentData == "value":
			self.stack.pop()
			if self.stack[-1] == "property":
				print "property_" + str(self.pv_counter) + "_value",self.value
				f_out.write("property_" + str(self.pv_counter) + "_value")
				f_out.write(" ")
				f_out.write(self.value)
				f_out.write("\n")
				self.pv_counter = self.pv_counter + 1
			elif self.stack[-1] == "qualifier":
				print "qualifier_" + str(self.qv_counter) + "_value",self.value
				f_out.write("qualifier_" + str(self.qv_counter) + "_value")
				f_out.write(" ")
				f_out.write(self.value)
				f_out.write("\n")
				self.qv_counter = self.qv_counter + 1
		elif self.currentData == "pickListItem":
			self.stack.pop()
			print "pickListItem_" + str(self.pl_counter),self.pickListItem
			f_out.write("pickListItem_" + str(self.pl_counter))
			f_out.write(" ")
			f_out.write(self.pickListItem)
			f_out.write("\n")
			self.pl_counter = self.pl_counter+1
		
		self.currentData = ""
	
#function to set data content to object	
	def characters(self, content):
	
		if self.currentData == "name":
			self.name = content.encode('utf-8')
		elif self.currentData == "value":
			self.value = content.encode('utf-8')
		elif self.currentData == "code":
			self.code = content.encode('utf-8')	
		elif self.currentData == "id":
			self.id = content.encode('utf-8')
		elif self.currentData == "namespace":
			self.namespace = content.encode('utf-8')
		elif self.currentData == "kind":
			self.kind = content.encode('utf-8')
		elif self.currentData == "primitive":
			self.primitive = content.encode('utf-8')
		elif self.currentData == "concept":
			self.concept = content.encode('utf-8')
		elif self.currentData == "range":
			self.range = content.encode('utf-8')
		elif self.currentData == "domain":
			self.domain = content.encode('utf-8')
		elif self.currentData == "inverseName":
			self.inverseName = content.encode('utf-8')
		elif self.currentData == "pickListItem":
			self.pickListItem = content.encode('utf-8')
					
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = DefHandler()
parser.setContentHandler(Handler)
parser.parse(file_path+"NDFRT_Public_2014.07.07_TDE.xml")
f_out.close()


	


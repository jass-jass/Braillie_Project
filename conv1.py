from PyPDF2 import PdfReader
import louis
import os



#create a directory
# Directory
directory = "translation_dir"
# Parent Directory path
parent_dir = "/home/sanjana/Documents/Braille_Project/"
# Path
path = os.path.join(parent_dir, directory)

tableList = ["unicode.dis","braille-patterns.cti","en-ueb-g1.ctb"]

if os.path.isdir(path):
	pass
else:
	os.mkdir(path)

#This below code opens a file and reads a file and converts the text into braillie which is stored in a diffrent file in translation_dir directory
with open("sample.pdf","rb") as f:
	pdf = PdfReader(f)
	no_of_pages = len(pdf.pages)
	if no_of_pages > 0:
		for page_id in range(no_of_pages):
			page_obj = pdf.pages[page_id]
			lines=page_obj.extract_text().splitlines()
			#print("\n","THIS IS PAGE",page_id ,"\n")
			#print(lines)
			translated = open("translation_dir"+"/"+"Page_"+str(page_id)+".BRL",'w')
			for line in lines:
				translated.write(louis.translateString(tableList,line)+ "\n")
			translated.close()
			



	

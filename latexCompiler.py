import csv
from pylatex import Document, Section, Subsection, Command, Package
from pylatex.utils import italic, bold, NoEscape

def writeBook(book,count,ids):
	doc.append(NoEscape("\hline"))
	if resourceType=="Textbooks":
		doc.append('Book Title: ')
		doc.append(italic(book))
	else:
		doc.append('Resource: ')
		doc.append(italic(book))
#target.write("        Copies: " + str(count) + "\n")
	doc.append('\nCopies: '+str(count)+"\n")
#target.write("        Barcode Number(s): " + str(ids) + "\n\n")
	doc.append('Barcode Number(s): '+str(ids)+"\n\n")
#target.write("        Actual Count:______________            \n")
	doc.append('Actual Count:___________\n\n')

def writeFileEnd(titlecount,bookcount):
#target.write("\n==============================================\n\n")
	doc.append(NoEscape("\hline"))
#target.write("    Title Count: " + str(tTitleCount) + "\n")
	doc.append('Title Count: '+str(tTitleCount)+"\n")
#target.write("    Item Count: " + str(tBookCount) + "\n\n")
	doc.append('Item Count: '+str(tBookCount)+"\n")
	doc.append("    Signature:___________________________________         Date:_______________\n" )


f = csv.reader(open('teachers.csv','r'))
pTeacher=''
teachers=0
for row in f:
	if row[3]=="6/10/2016" and not row[2]=="Library Materials":
		cTeacher=row[0]
		if not cTeacher==pTeacher:
			if not pTeacher=='':
				# Finish Current Book
				writeBook(pBook,cBookCount,bookIDs)

				# Print totals for pTeacher
				writeFileEnd(tTitleCount,tBookCount)
#target.close()
				doc.generate_pdf(teacherString)


			# Update teacher info
			teacherString=cTeacher.translate(None, " .-")
			pTeacher=cTeacher
			teachers = teachers+1
			# Open New File
#filename = teacherString + ".txt"
#target = open(filename,'w')
			doc=Document('basic')
#target.write(cTeacher + "    (" + row[1] + ")" + "\n\n")
			doc.packages.append(Package('fullpage'))
			doc.create(Section(cTeacher,numbering=0))

			# Process Book
			cBook=row[7]
			bookIDs=[row[5]]
			resourceType=row[2]
			pBook=cBook
			cBookCount=1
			tBookCount=1
			tTitleCount=1
		else:
			cBook=row[7]
			if not cBook==pBook:
				writeBook(pBook,cBookCount,bookIDs)
				bookIDs=[row[5]]
				resourceType=row[2]
				pBook=cBook
				cBookCount=1
				tTitleCount=tTitleCount+1
			else:
				cBookCount=cBookCount+1
				bookIDs.append(row[5])
			tBookCount = tBookCount+1

# finish last teacher
# Finish Current Book
writeBook(pBook,cBookCount,bookIDs)
pBook=cBook
cBookCount=1

# Print totals for pTeacher
writeFileEnd(tTitleCount,tBookCount)

#target.close()
doc.generate_pdf(teacherString)

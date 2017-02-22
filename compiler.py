import csv

def writeBook(book,count,ids):
	target.write("-----------------------------------------------------\n")
	if resourceType=="Textbooks":
		target.write("    Book Title: " + book + "\n")
	else:
		target.write("    Resource: " + book + "\n")
	target.write("        Copies: " + str(count) + "\n")
	target.write("        Barcode Number(s): " + str(ids) + "\n\n")
	target.write("        Actual Count:______________            \n")

def writeFileEnd(titlecount,bookcount):
	target.write("\n==============================================\n\n")
	target.write("    Title Count: " + str(tTitleCount) + "\n")
	target.write("    Item Count: " + str(tBookCount) + "\n\n")
	target.write("    Signature:___________________________________         Date:_______________\n" )


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
				target.close()


			# Update teacher info
			teacherString=cTeacher.translate(None, " .-")
			pTeacher=cTeacher
			teachers = teachers+1
			# Open New File
			filename = teacherString + ".txt"
			target = open(filename,'w')
			target.write(cTeacher + "    (" + row[1] + ")" + "\n\n")

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

target.close()

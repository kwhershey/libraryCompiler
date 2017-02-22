import csv

def writeBook(book,count,ids):
	target.write("-----------------------------------------------------\n")
	if resourceType=="Textbooks":
		target.write("    Book Title: " + book + "\n")
	else:
		target.write("    Resource: " + book + "\n")
	target.write("        Copies: " + str(count) + "\n")
	target.write("        Barcode Number(s): " + str(ids) + "\n")

f = csv.reader(open('teachers.csv','r'))
pTeacher=''
teachers=0
for row in f:
	if row[3]=="6/10/2016" and not row[2]=="Library Materials":
		cTeacher=row[0]
		if not cTeacher==pTeacher:
			if not pTeacher=='':
				# Finish Current Book
				target.write("-----------------------------------------------------\n")
				if resourceType=="Textbooks":
					target.write("    Book Title: " + pBook + "\n")
				else:
					target.write("    Resource: " + pBook + "\n")
				target.write("        Copies: " + str(cBookCount) + "\n")
				target.write("        Barcode Number(s): " + str(bookIDs) + "\n")

				# Print totals for pTeacher
				target.write("\n==============================================\n\n")
				target.write("    Title Count: " + str(tTitleCount) + "\n")
				target.write("    Item Count: " + str(tBookCount) + "\n")
				target.close()


			# Update teacher info
			teacherString=cTeacher.translate(None, " .-")
			pTeacher=cTeacher
			teachers = teachers+1
			# Open New File
			filename = teacherString + ".txt"
			target = open(filename,'w')
			target.write(teacherString + "(" + row[1] + ")" + "\n")

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
				#print "    You have " + str(cBookCount) + " copies of " + "\"" + pBook + "\""
				target.write("-----------------------------------------------------\n")
				if resourceType=="Textbooks":
					target.write("    Book Title: " + pBook + "\n")
				else:
					target.write("    Resource: " + pBook + "\n")
				target.write("        Copies: " + str(cBookCount) + "\n")
				target.write("        Barcode Number(s): " + str(bookIDs) + "\n")
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
#print "    You have " + str(cBookCount) + " copies of " + "\"" + pBook + "\""
target.write("-----------------------------------------------------\n")
if resourceType=="Textbooks":
	target.write("    Book Title: " + pBook + "\n")
else:
	target.write("    Resource: " + pBook + "\n")
target.write("        Copies: " + str(cBookCount) + "\n")
target.write("        Barcode Number(s): " + str(bookIDs) + "\n")
pBook=cBook
cBookCount=1

# Print totals for pTeacher
target.write("\n==============================================\n\n")
target.write("    Title Count: " + str(tTitleCount) + "\n")
target.write("    Item Count: " + str(tBookCount) + "\n")

target.close()



print "\nThere are " + str(teachers) + " teachers."

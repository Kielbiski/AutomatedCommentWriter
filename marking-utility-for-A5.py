#Jeremy Kielbiski jeremykielbiski@scs.carleton.ca
#Robert Collier robertcollier3@cunet.carleton.ca
import os
import math
import sys
import shutil
from os import system, name, getcwd, listdir, path
from zipfile import *
from time import sleep
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

# download the assignment submissions and extract to the working directory
# download the offline grading worksheet to the working directory
# download a plaintext export of the grades to the working directory

# these are the names that students were instructed to use for their archive
archivename = "a5.zip"
q1submission = "a5q1.py"
q2submission = "a5q2.py"
edit = """

print("Please consult the generator and see if the expected output matches this output.")
print("Their program produces: ")
testList = []
try:
    for i in range(22):
        testList.append(functionName1(i+1))
    print("Base cases: ")
    for i in range(6):
        print("f(" + str(i) + ") = " + str(testList[i]))
    print("Rest of sequence: ")
    for i in range(6,21):
        print("f(" + str(i) + ") = " + str(testList[i]))
except Exception as e:
    print()
    print(e)
    print(type(e))
    print()
    input("1st function crashed, press enter to continue. ")
try:
    print(functionName2(20))
    input("Press enter to quit. ")
except Exception as e:
    print()
    print(e)
    print(type(e))
    print()
    input("Program crash, press enter to quit. ")
"""
editPartStart = """
try:

"""
editPartEnd = """
except Exception as e:
    print()
    print(e)
    print(type(e))
    print()
    input("Program crash, press enter to quit. ")
"""
# initialize an empty list to store the folders
folders = []

offlinegradingworksheet = {}
handle = open("offline-grading-worksheet.csv", "r")
for line in handle:
	data = line.split(",")
	offlinegradingworksheet[data[0]] = data[2]
handle.close()
	
plaintextgradesexported = {}
handle = open("plaintext-grades-exported.csv", "r")
for line in handle:
	data = line.split(",")
	plaintextgradesexported[data[2]] = data[3]
handle.close()

def main():
	
	# list the contents (including folders) of the current working directory
	contents = listdir(getcwd())

	# for each item in the current working directory...
	for item in contents:

		# ...join the item name to the path...
		possible = path.join(getcwd(), item)
		
		# ...and check if it is a directory...
		if path.isdir(possible) and not item == "__pycache__":
		
			# ...and, if so, add it to the list of folders
			folders.append(possible)
	if name == "nt":
			system('cls')
	else:
		system('clear')

	selectionFlag = 0
	for i in range(100):
				print('#',end = "")
	print()
	print()
	print("Please mark slowly and accurately to avoid remarking request forms later on.")
	print()
	for i in range(100):
		print('#',end = "")
	print()
	for i in range(60):
		sleep(0.05)
	while True:
		TAname = input("Please type your name in the format FirstName LastName (ie. John Smith): \n")
		if len(TAname.split()) == 2:
			TAfirstName,TAlastName = TAname.split()
			TAemail = str(TAfirstName.lower() + "." + TAlastName.lower() + "@carleton.ca")
			break
		else:
			print("\n_________________________________________________________________________________________\n")
			print("Input Error: Please type your name in the format requested.")
			print("\n_________________________________________________________________________________________\n")
	"""
	while True:
		section = input("Which section are you marking? (A/B): \n").lower()
		if (section == 'a'):
			selectionFlag = 1
			break
		elif (section == 'b'):
			sectionFlag = 2
			break
		else:
			print("\n_________________________________________________________________________________________\n")
			print("Input Error: Please type in either A or B.")
			print("\n_________________________________________________________________________________________\n")
	"""
	

	input("\n"+"Press enter to start the generator."+"\n")
	target = open("marking-utility-a5-output.txt", 'w')
	target.write("Assignment 4 Marking Output for " + TAname + "\n")
	target.close()
	mainDir = os.getcwd()
	# visit each folder...
	for folder in folders:
		# clear the screen
		mark = 0
		mark1 = 0
		mark2 = 0
		comments = ""
		extraComments = ""
		editCopy = edit
		"""
		if name == "nt":
			system('cls')
		else:
			system('clear')
		"""
		###################################################################################################################
		# ...and find the zip file for the submission and extract the contents...
		try:
			archive = ZipFile(folder + "\\" + archivename, "r")
			archive.extractall(folder)

		except Exception as e: 
			print()
			print("Could not open 'a5.zip' from", folder)
			print()
			comments = comments + "[GENERAL] Your zip file was named incorrectly.\n"
			print(type(e))
			print(e)
			print()
			print("To manually correct this error you may need to rename the zip file and extract the contents")
			print()
			choice = input("If you were able to manually correct this error, <enter 'Y'>; Otherwise, <enter 'N'>: ").lower()
			while not(choice.lower() == 'y' or choice.lower() == 'n'):
				choice = input("< type either Y or N and press enter >")
			if input == 'n':
				# write the record so far
				continue
		###################################################################################################################		
		# ...then look up the corresponding student number...

		try:
			label = folder.replace(getcwd(),"...")
			underscore1 = label.find("_")
			underscore2 = label.find("_", underscore1+1)
			participantid = label[underscore1+1:underscore2]
			email = offlinegradingworksheet['"Participant ' + participantid + '"']
			studentid = plaintextgradesexported[email]
			studentNameList = email.replace('@','.')
			studentName = studentNameList.split(".")
			studentname = str(studentName[0] + " " + studentName[1]).title()
		
		except Exception as e:
			print("Could not locate the owner of", folder)
			comments = comments + "[GENERAL] No submission.\n"
			mark = 0
			print()
			print(type(e))
			print(e)
			continue

		###################################################################################################################
		try:
			target = open("marking-utility-a5-output.txt", 'a')
			target.write("_________________________________________________________________________________________\n")
			target.write(studentname + "     " + str(studentid) + "     " + email + "\n")
			target.close()
			print()
			print(folder, participantid, studentname, email, studentid)
			print()
			handle = open(folder + "\\" + q1submission, "r")
			submission = handle.read()
			handle.close()
			
		except Exception as e: 
			print()
			print("Could not open 'a5q1.py' from ", folder)
			comments = comments + "[GENERAL] Either your zip file contained a folder (not just the two .py files) OR your a5q1.py file was named incorrectly (-3 marks).\n" 
			mark = mark - 3
			print()
			print(type(e))
			print(e)
			print()
			print("To manually correct this error, you may need to rename the file to 'a5q1.py' or move it out of a folder.")
			print()
			choice = input("If you were able to manually correct this error, <enter 'Y'>; Otherwise, <enter 'N'>: ").lower()
			while not(choice == 'y' or choice == 'n'):
				choice = input("< type either Y or N and press enter >")
			if input == 'n':
				# write the record so far
				comments = comments + "\nPart 1 was not submitted (mark of zero for this part)."
				mark1 = 0
				continue
		###################################################################################################################
		# ...and then finally try to run the submission...
		try:
			for i in range(100):
				print('#',end = "")
			print()
			print("+++ Student's Source Code +++".center(100))
			print()
			print()
			handle1 = open(folder + "\\" + q1submission)
			filedata = handle1.read()
			handle1.close()
			clean = []
			for char in filedata:
				if ord(char) < 256:
					clean.append(char)
			part1 = "".join(clean)
			print(part1)
			print()
			print("If you have run the utility on this student's code before please remove the appended block of code at the bottom at the bottom. The code to remove is listed at the top.")
			print()
			while True:
				functionName1 = input("What is the name of their first function (element finder)? Please type it exactly as it is written in their code. ")
				print()
				check = input("Are you sure that you have written the function name perfectly? (Y/N) ").lower()
				print()
				while not (check == 'y' or check == 'n'):
					check = input("Please type in either Y or N.").lower()
					print()
				if check == 'y':
					break
			while True:
				functionName2 = input("What is the name of their second function (list creator)? Please type it exactly as it is written in their code. ")
				print()
				check = input("Are you sure that you have written the function name perfectly? (Y/N) ").lower()
				print()
				while not (check == 'y' or check == 'n'):
					check = input("Please type in either Y or N.").lower()
					print()
				if check == 'y':
					break
			try:
				handle = open(folder + "\\" + q1submission)
				programContents1 = handle.read()
				handle.close()
				programContents1 = programContents1.replace('\t','    ')
				programContents1 = programContents1.replace('\n','\n    ')
				handle = open(folder + "\\" + q1submission, 'w')
				handle.write(editPartStart)
				handle.write(programContents1)
				handle.write(editPartEnd)
				handle.close()
				handle = open(folder + "\\" + q1submission, 'a')
				editCopy = editCopy.replace("functionName1", functionName1)
				editCopy = editCopy.replace("functionName2", functionName2)
				handle.write(editCopy)
				handle.close()
				editCopy = edit
			except:
				print("File reading failed. ")
				print("******************************")
			print()
			print()
			handle1 = open(folder + "\\" + q1submission)
			filedata = handle1.read()
			handle1.close()
			clean = []
			for char in filedata:
				if ord(char) < 256:
					clean.append(char)
			part1 = "".join(clean)
			print(part1)
			print()
			recursionProcess = Popen([executable, folder + "\\" + q1submission], creationflags = CREATE_NEW_CONSOLE)
			print("If their program just opened and closed immediately then it crashed. Please manually open a command prompt window and navigate to their folder and try to run their program.\n")
			for i in range(100):
				print('#',end = "")
			print()
			print()
			print("Part 1".center(100))
			print()
			shutil.copy(mainDir + '\\' 'generator.py',folder)
			os.chdir(folder)
			generatorProcess = Popen([executable, 'generator.py', studentid], creationflags = CREATE_NEW_CONSOLE)
			os.chdir(mainDir)
			print()
			print("Do not close the generator that has opened in another window.")
			print()
			for i in range(100):
				print('#',end = "")
			print()
			print()
			print("+++ Part 1 Marking +++".center(100))
			print()
			print(("The generator specific to " + str(studentname) + " has opened in another window.").center(100))
			print("Please use ALT-TAB to efficiently go between this utility and the generator.".center(100))
			print()
			for i in range(100):
				print("#", end = "")
			print()
			print("+++ Marking Penalties +++".center(100))
			print()
			if input("Does it fail to use recursion? (Y/N) ").lower() == 'y':
				mark1 = mark1 - 999
				comments = comments + ("[Part 1] Your program was not recursive and therefore did not follow the instructions (mark of zero for this part).\n")
			print()
			"""
			if input("Does it use the 'create list of n elements' function to call the 'find nth element' function? (Y/N) ").lower() == 'y':
				mark1 = mark - 4
				comments = comments + ("[Part 1] Your program uses the 'create list of n elements' function to call the 'find nth element' function.\n\tThis is incredibly slow (running time of O(n!)) and should have been avoided by designing your program to be more efficient (-4).\n")
			print()
			"""
			if input("Does it crash with a division/modulo by zero error? (Y/N) ").lower() == 'y':
				mark1 = mark - 4
				comments = comments + ("[Part 1] Your program crashes with a division/modulo by zero error (-4).\n")
			print()
			if input("Do either of their functions perform unneccessary calls (for example by finding the same element's value over and over again)? (Y/N) ").lower() == 'y':
				mark1 = mark1 + 2
				while True:
					print()
					findOne = input("Which function was it? Please name it exactly as it is written in the code. ")
					print()
					check = input("Are you sure that you have written the function name perfectly? ").lower()
					print()
					while not (check == 'y' or check == 'n'):
						check = input("Please type in either Y or N.")
						print()
					if check == 'y':
						break
				comments = comments + ("[Part 1] Your " + findOne + " program calls functions unneccessarily (for example by finding the same element's value over and over again) (-2 marks).\n")
			print()
			for i in range(100):
				print("#", end = "")
			print()
			print("+++ Marking Criteria +++".center(100))
			print()
			print(("Please reference the source code for part 1 from " + studentname + " printed above.").center(100))
			print()
			if input("Are their base cases correct? (Y/N) ").lower() == 'y':
				mark1 = mark1 + 2
			else:
				comments = comments + ("[Part 1] Your program's base cases did not match the base cases provided by the generator (-2 marks).\n")
			print()
			if input("Does their output for the first function (find nth element) match the expected output? (Y/N) ").lower() == 'y':
				mark1 = mark1 + 6
			else:
				comments = comments + ("[Part 1] Your program's first function's (find nth element) output did not match with the actual nth element of the given sequence (-6 marks).\n")
			print()
			if input("Does their output for the second function (create list of n elements) match the expected output? (Y/N) ").lower() == 'y':
				mark1 = mark1 + 6
			else:
				comments = comments + ("[Part 1] Your program's second function's (create list of n elements) output did not match with the actual list of n elements of the given sequence.(-6 marks).\n")
			print()
			if mark1 < 0:
				mark1 = 0
			mark = mark + mark1
			print("Part 1: " + str(mark1) + "/14")
			comments = comments + ("Part 1: " + str(mark1) + "/14\n")
			print()

		except Exception as e: 
			print()
			print("Utility crashed. ")
			comments = comments + ("[Part 1] Your code for part 1 crashed.\n")
			comments = comments + ("Part 1: 0/14\n")
			print()
			print(type(e))
			print(e)
		###################################################################################################################
		try:
			handle = open(folder + "\\" + q2submission, "r")
			submission2 = handle.read()
			handle.close()
			
		except Exception as e: 
			print()
			print("Could not open 'a5q2.py' from", folder) 
			print()
			comments = comments + "[GENERAL] Your a5q2.py file was named incorrectly.\n"
			mark = mark - 5
			print(type(e))
			print(e)
			print()
			print("To manually correct this error, you may need to rename the file to 'a5q2.py' or move it out of a folder")
			print()
			choice = input("If you were able to manually correct this error, <enter 'Y'>; Otherwise, <enter 'N'>: ").lower()
			while not(choice.lower() == 'y' or choice.lower() == 'n'):
				choice = input("< type either Y or N and press enter >")
			if input == 'n':
				# write the record so far
				comments = comments + "\nPart 2 was not submitted (mark of zero for this part)."
				mark2 = 0
				continue
		###################################################################################################################
		try:
			for i in range(100):
				print('#',end = "")
			print()
			print()
			print("Part 2".center(100))
			print()
			handle = open(folder + "\\" + q2submission)
			programContents = handle.read()
			handle.close()
			programContents = programContents.replace('\t','    ')
			programContents = programContents.replace('\n','\n    ')
			handle = open(folder + "\\" + q2submission, 'w')
			handle.write(editPartStart)
			handle.write(programContents)
			handle.write(editPartEnd)
			handle.close()
			dictionaryProcess = Popen([executable, folder + "\\" + q2submission], creationflags = CREATE_NEW_CONSOLE)		
			for i in range(100):
				print("#", end = "")
			print()
			print("+++ Student's Source Code +++".center(100))
			print()
			print()
			handle2 = open(folder + "\\" + q2submission)
			filedata = handle2.read()
			handle2.close()
			clean = []
			for char in filedata:
				if ord(char) < 256:
					clean.append(char)
			part2 = "".join(clean)
			print(part2)
			for i in range(100):
				print('#',end = "")
			print()
			print("+++ Part 2 Marking +++".center(100))
			print()
			print(("The homoglyph program written by " + str(studentname) + " has opened in another window.").center(100))
			print()
			print(("--- Please try every function in the program from " + studentname + " in the other window. ---").center(100))
			print()
			for i in range(100):
				print("#", end = "")
			print()
			print()
			print("If their program opened and closed immediately then it crashed. Please manually open a command prompt window and navigate to their folder and try to run their program to see the error.")
			print()
			for i in range(100):
				print("#", end = "")
			print()
			print()
			print("If their program crashed, please answer 'N' for all of the Part 2 criteria.")
			print()
			for i in range(100):
				print("#", end = "")
			print()
			print()
			print("+++ Marking Penalties +++".center(100))
			print()
			if input("Does their program fail to create a dictionary? (Y/N) ").lower() == 'y':
				mark2 = mark2 -999
				comments = comments + ("[Part 2] Your program does not create a dictionary and therefore did not follow the instructions (mark of zero for this part).\n")
			for i in range(100):
				print("#", end = "")
			print()
			print()
			print("+++ Marking Criteria +++".center(100))
			print()
			print(("Please reference the source code for part 2 from " + studentname + " printed above.").center(100))
			print()
			for i in range(100):
				print("#", end = "")
			print()
			print()
			if input("Does their program read in the your-assigned-glyphs.dat file? (Y/N) ").lower() == 'y':
				mark2 = mark2 + 4
			else:
				comments = comments + ("[Part 2] Your program did not read in the your-assigned-glyphs.dat file (-4 marks).\n")
			print()
			if input("Does their program store values as lists? (Y/N) ").lower() == 'y':
				mark2 = mark2 + 4
			else:
				comments = comments + ("[Part 2] Your program does not store values as lists (-4 marks).\n")
			print()
			if input("Does their program store all possible values for a specific key (if there are no duplicates type Y)? (Y/N) ").lower() == 'y':
				mark2 = mark2 + 4
			else:
				comments = comments + ("[Part 2] Your program does not all possible values for a specific key (-4 marks).\n")
			print()
			if input("Does their program translate properly? (Y/N) ").lower() == 'y':
				mark2 = mark2 + 8
			else:
				comments = comments + ("[Part 2] Your program does not translate properly (-8 marks).\n")
			print()
			if input("Does their first generator-given function work properly? (Y/N) ").lower() == 'y':
				mark2 = mark2 + 6
			else:
				comments = comments + ("[Part 2] Your program's first generator-given function does not work properly (-6 marks).\n")
			print()
			if input("Does their second generator-given function work properly? (Y/N) ").lower() == 'y':
				mark2 = mark2 + 6
			else:
				comments = comments + ("[Part 2] Your program's second generator-given function does not work properly (-6 marks).\n")
			print()
			if input("Does their quit function work properly? (Y/N) ").lower() == 'y':
				mark2 = mark2 + 4
			else:
				comments = comments + ("[Part 2] Your program's quit function does not work properly (-4 marks).\n")
			print()
			if mark2 < 0:
				mark2 = 0
			mark = mark + mark2
			print("Part 2: " + str(mark2) + "/36")
			comments = comments + ("Part 2: " + str(mark2) + "/36\n")
			print()

		except Exception as e:
			print()
			print("Utility crashed. ")
			comments = comments + ("[Part 2] Your code for part 2 crashed.\n")
			comments = comments + ("Part 2: 0/36\n")
			print()
			print(type(e))
			print(e)
		###################################################################################################################
		print()
		for i in range(100):
				print("#", end = "")
		print()
		print("+++ General Marking Criteria +++".center(100))
		print()
		print()
		if input("Did they include their name AND student number in the headers of BOTH files? (Y/N) - ").lower() == 'n':
			mark = mark - 5
			comments = comments + ("[GENERAL] Name or student number was missing from one or both files (-5 marks).\n")
		print()
		if input("Were there proper citations in the header of either file) (Y/N) - ").lower() == 'n':
			mark = mark - 5
			comments = comments + ("[GENERAL] Citations were missing from both files (-5 marks).\n")
		print()
		if mark < 0:
			mark = 0
		print("Mark: " + str(mark) + "/54")
		print()
		for i in range(100):
				print("#", end = "")
		print()
		extra = input("\nDo you have any extra comments? (Y/N)\n").lower()
		while not(extra == 'y' or extra == 'n'):
			extra = input("Please type in either Y or N.\n")
		if extra == 'y':
			extraComments = input("Please type them below:\n")
			comments = comments + "\nExtra Comments:\n" + extraComments
		print()
		for i in range(100):
				print("#", end = "")
		print()
		shutil.move(folder + "\\" + 'generator.py',mainDir + "\\" + 'generator.py')
		try:
			generatorProcess.kill()
		except Exception as e:
			print("No generator process available to kill.\n")
			print()
			print(type(e))
			print(e)
			print()
		try:
			recursionProcess.kill()
		except Exception as e:
			print("No recursion process available to kill.\n")
			print()
			print(type(e))
			print(e)
			print()
		try:
			dictionaryProcess.kill()
		except Exception as e:
			print("No dictionary process available to kill.\n")
			print()
			print(type(e))
			print(e)
			print()
		unroundedMark = mark / 50 * 100
		markInPercent = math.ceil(unroundedMark * 100) / 100
		target = open("marking-utility-a5-output.txt", 'a')
		###################################################################################################################		
		input("\n"+"Press enter to continue."+"\n")
		target.close()
	print("Reached the end of student folders. ")

if __name__ == "__main__":
	main()

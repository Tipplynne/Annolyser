	#Menu Interfacer in that Menu.py file
#-------------------------------------------------------------------------------------------------------------------------------------------


def options(menu):
	import gffloader
	import fastaloader
	qq=0
	tt=0


	#Load fasta files:
#-------------------------------------------------------------------------------------------------------------------------------------------

	if menu == "1" or menu == "F":
		import fastaloader

		f = input("Enter the fasta file name to be entered, character for character : ")
		fastaloader.fasta_loader(f)
		qq=0
		for seq in fastaloader.slist:
			qq = qq + 1
		
		while f != '':

			f = input("Enter another fasta file name to be entered, character for character, or press [Enter] to go back to the Menu: ")
	
			if f == "":
				return f
				break
				
			else:
				fastaloader.fasta_loader(f)
				
				for seq in fastaloader.slist:
					qq = qq + 1
	

		#Load gff files	#-------------------------------------------------------------------------------------------------------------------------------------------- 

	elif menu == "2" or menu == "G":
		import gffloader

		g = input("Enter the gff file to be entered, character for character : ")
		gffloader.gff_loader(g)

		while g != '':

			g = input("Enter another gff file to be entered, or press [Enter] to go back to the Menu: ")

			if g == "":
				
				return g
				break

			else:
				gffloader.gff_loader(g)
				

		#Annotation explorer:	#---------------------------------------------------------------------------------------------------------------------------------------------

	elif menu == "3" or menu == "A":

		seq1 = input("Which sequence's annotations would you like to view? \n")

		seq2 = []

		for anno in gffloader.alist:

			seq2.append(anno.SEQREF)

		noanno = 0

		noanno = seq2.count(seq1)
	
		if noanno == 0:

			print("Sequence %s has no annotations. \n\n" %(seq1))
			return ""

		else:
			 
			print("The sequence %s has %i annotations:\n" %(seq1, noanno))

		tempdiction = {}

		for seq in fastaloader.slist:
			tempdiction[seq.IDY] = seq.SEQ

		tempsublist = []
		templist = []

		for anno in gffloader.alist:
				tempsublist = []
				tempsublist.append(anno.SEQREF)
				tempsublist.append(anno.SRC)
				tempsublist.append(anno.FEAT)
				tempsublist.append(int(anno.START))
				tempsublist.append(int(anno.STOP)) 
				tempsublist.append(anno.SCORE)
				tempsublist.append(anno.STRAND)
				tempsublist.append(anno.FSE)
				tempsublist.append(anno.GRP)
		
				if seq1 == tempsublist[0]:
					templist.append(tempsublist)


		for p in range(len(templist)):

			smin10 = 0
			smax10 = 0
			left = ''
			right = ''
			middle = ''

			if seq1.lower() not in tempdiction:	#warning for no seq loaded

				input("Annotation %s. %s(%s)\n------------------------------------------------------------\nWARNING: No sequence loaded for sequence id %s!!!\nSTART:   %i\nSTOP:   %i\nSCORE:   %s \nSTRAND:   %s\nPHASE:   %s\nGROUP:    %s\n\nPress [enter]  for the next annotation, else [M] to return to Menu: \n" %((p+1), templist[p][2], templist[p][1], seq1, int(templist[p][3]), int(templist[p][4]), templist[p][5], templist[p][6], templist[p][7], templist[p][8]))

		
		
			else:
				if (int(templist[p][3])-1) > 10:
					smin10 = int(templist[p][3])-11
				else:
					smin10 = 1

				if (int(templist[p][4])+1) < len(tempdiction[str(templist[p][0]).lower()])-11:
					smax10 = int(templist[p][4])+11
				else:
					smax10 = len(tempdiction[str(templist[p][0]).lower()])

				left = tempdiction[str(templist[p][0]).lower()][smin10:int(templist[p][3])-1].lower()
				middle = tempdiction[str(templist[p][0]).lower()][int(templist[p][3]):int(templist[p][4])]
				right = tempdiction[str(templist[p][0]).lower()][int(templist[p][4])+1:smax10].lower()  #formatting seq portions

				input("Annotation %s. %s(%s)\n------------------------------------------------------------\n...(%i)\n%s%s%s\n(%i)...\nSCORE:   %s\nSTRAND:   %s\nPHASE:   %s\nGROUP:    %s\n\nPress [enter]  for the next annotation, else [M] to return to Menu: \n" %((p+1), templist[p][2], templist[p][1], smin10, left, middle, right, smax10, templist[p][5], templist[p][6], templist[p][7], templist[p][8]))

		return ""


		#Annotation Creator	#------------------------------------------------------------------------------------------------------------------------------------------------

	elif menu == "4" or menu == "C":

		ant = input("For which sequence would you like to create annotations? ")	#first annotation entry
		s = input("Source : ")
		fe = input("Feature : ")
		sta = input("Start : ")
		sto = input("Stop : ")
		sco = input("Score : ")
		st = input("Strand : ")
		ph = input("Phase : ")
		gr = input("Group : ")

		anno = gffloader.Annotate(ant, s, fe, sta, sto, sco, st, ph, gr)
		gffloader.alist.append(anno)

		temp2diction = {}

		for seq in fastaloader.slist:
			temp2diction[seq.IDY] = seq.SEQ

		smin10 = 0
		smax10 = 0
		left = ''
		right = ''
		middle = ''
		annan = 'y'

		if ant.lower() not in temp2diction:

			annan = input("New Annotation : %s(%s)\n------------------------------------------------------------\nWARNING: No sequence loaded for sequence id %s!!!\nSTART:   %i\nSTOP:   %i\nSCORE:   %s \nSTRAND:   %s\nPHASE:   %s\nGROUP:    %s\nWould you like to create another annotation for this sequence ID? [y/n] \n" %(fe, s, ant, int(sta), int(sto), sco, st, ph, gr))
	
	
		else:
			if (int(sta)-1) > 10:
				smin10 = int(sta)-11
			else:
				smin10 = 1

			if (int(sto)+1) < len(temp2diction[ant.lower()])-11:
				smax10 = int(sto)+11
			else:
				smax10 = len(temp2diction[ant.lower()])

			left = temp2diction[ant.lower()][smin10:int(sta)-1].lower()
			middle = temp2diction[ant.lower()][int(sta):int(sto)]
			right = temp2diction[ant.lower()][int(sto)+1:smax10].lower()

			annan = input("New Annotation : %s(%s)\n------------------------------------------------------------\n...(%i)\n%s%s%s\n(%i)...\nSCORE:   %s\nSTRAND:   %s\nPHASE:   %s\nGROUP:    %s\nWould you like to create another annotation for this sequence ID? [y/n] \n\n" %(fe, s, smin10, left, middle, right, smax10, sco, st, ph, gr))



		while annan == "y":					#subsequent annotation entries

			ant = input("For which sequence would you like to create annotations? ")
			s = input("Source : ")
			fe = input("Feature : ")
			sta = input("Start : ")
			sto = input("Stop : ")
			sco = input("Score : ")
			st = input("Strand : ")
			ph = input("Phase : ")
			gr = input("Group : ")

			anno = gffloader.Annotate(ant, s, fe, sta, sto, sco, st, ph, gr)
			gffloader.alist.append(anno)

			temp2diction = {}

			for seq in fastaloader.slist:
				temp2diction[seq.IDY] = seq.SEQ

			smin10 = 0
			smax10 = 0
			left = ''
			right = ''
			middle = ''

			if ant.lower() not in temp2diction:

				annan = input("New Annotation : %s(%s)\n------------------------------------------------------------\nWARNING: No sequence loaded for sequence id %s!!!\nSTART:   %i\nSTOP:   %i\nSCORE:   %s \nSTRAND:   %s\nPHASE:   %s\nGROUP:    %s\n\nWould you like to create another annotation for this sequence ID? [y/n] \n" %(fe, s, ant, int(sta), int(sto), sco, st, ph, gr))
	
	
			else:
				if (int(sta)-1) > 10:
					smin10 = int(sta)-11
				else:
					smin10 = 1

				if (int(sto)+1) < len(temp2diction[ant.lower()])-11:
					smax10 = int(sto)+11
				else:
					smax10 = len(temp2diction[ant.lower()])

				left = temp2diction[ant.lower()][smin10:int(sta)-1].lower()
				middle = temp2diction[ant.lower()][int(sta):int(sto)]
				right = temp2diction[ant.lower()][int(sto)+1:smax10].lower()

				annan = input("New Annotation : %s(%s)\n------------------------------------------------------------\n...(%i)\n%s%s%s\n(%i)...\nSCORE:   %s\nSTRAND:   %s\nPHASE:   %s\nGROUP:    %s\n\nWould you like to create another annotation for this sequence ID? [y/n] \n" %(fe, s, smin10, left, middle, right, smax10, sco, st, ph, gr))

		return ""
	
		#Export to File:	#---------------------------------------------------------------------------------------------------------------------------------------------	

	elif menu == "5" or menu == "X":

		ex = input("Filter by sequence ID or [all]? ")
		name = input("File path : ")

		mkgff = open(str(name), "w")

		temp3diction = {}

		for seq in fastaloader.slist:
			temp3diction[seq.IDY] = seq.SEQ

		if ex == "all":
			tempsublist = []

			for anno in gffloader.alist:
					tempsublist = []
					tempsublist.append(anno.SEQREF)
					tempsublist.append(anno.SRC)
					tempsublist.append(anno.FEAT)
					tempsublist.append(anno.START)
					tempsublist.append(anno.STOP) 
					tempsublist.append(anno.SCORE)
					tempsublist.append(anno.STRAND)
					tempsublist.append(anno.FSE)
					tempsublist.append(anno.GRP)
		
					mkgff.write("\t".join(tempsublist)+"\n")	

		else:
			tempsublist = []

			for anno in gffloader.alist:
					tempsublist = []
					tempsublist.append(anno.SEQREF)
					tempsublist.append(anno.SRC)
					tempsublist.append(anno.FEAT)
					tempsublist.append(anno.START)
					tempsublist.append(anno.STOP)
					tempsublist.append(anno.SCORE)
					tempsublist.append(anno.STRAND)
					tempsublist.append(anno.FSE)
					tempsublist.append(anno.GRP)
		
					if ex == tempsublist[0]:
						mkgff.write("\t".join(tempsublist)+"\n")


		mkgff.close()

		return input("FILE SAVED.\nPress [Enter] to go back to the Menu.")

		#Quit:
#-------------------------------------------------------------------------------------------------------------------------------------------
	
	elif menu == "6" or menu == "Q":

		last = input("Do you want to exit [Enter] or do you want go back to the menu? (M)")

		if last == "":
			return "exit"

		if last == "M":
			return ""

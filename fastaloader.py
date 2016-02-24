slist = []
class Sequence:
	SEQ = None
	IDY = None

	def toString(self):
		return self.SEQ+"\n"

	def __init__(self, seq, idy): # Creating "Sequence" Class
		self.SEQ = seq
		self.IDY = idy
             		

						
def fasta_loader(FAST):

	start = open(FAST, "r")
	newfile = start.read()
	stringlist = []
	seqno = newfile.count(">")

	if seqno > 1:
		stringlist = newfile.split("\n\n")	#split file into seq entries
	else:
		stringlist = []
		stringlist.append(newfile)

	stringlister = []

	for gt in range(len(stringlist)):
		stringlist[gt] = stringlist[gt].split(">")
		stringlister.append(stringlist[gt][1])			#remove ">" from seq ID's
		

	for k in range(len(stringlister)):
		stringlister[k] = stringlister[k].split("\n")		#split entries into base lines and seq ID


	keys = []

	for l in range(seqno):
		keys.append(stringlister[l][0])
		stringlister[l].remove(stringlister[l][0])		#remove seq ID's after saving them to a keylist

	keys2 = [change.lower() for change in keys]

	diction = {}

	for i in range(seqno):
		diction[keys2[i]] = ''.join(stringlister[i])		#join baselines into a single string minus \n formatting, whiles filling a 										dictionary


	for key in diction:									
		print("Sequence %s loaded; %i Residues\n" %(key.upper(), int(len(diction[key]))))


	for key in diction:
		seq = Sequence(diction[key],key)
		slist.append(seq)					#moving newly loaded sequences to class "Sequence"
		
		#I chose the alternative; to add this object to the list here and not in the constructor:
		#slist.append(seq) 




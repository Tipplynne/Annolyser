alist = []	#list that keeps original seq ID refs (allows calling for class objects in menu_mod.py)
class Annotate:
	SEQREF = None
	SRC = None
	FEAT = None
	START = None
	STOP = None
	SCORE = None
	STRAND = None
	FSE = None
	GRP = None

	def __init__(self, seqref, src, feat, start, stop, score, strand, fse, grp): 
		self.SEQREF = seqref
		self.SRC = src
		self.FEAT = feat
		self.START = start
		self.STOP = stop
		self.SCORE = score
		self.STRAND = strand
		self.FSE = fse
		self.GRP = grp			#GFF features Class "Annotate" created

def gff_loader(GFF):

	start = open(GFF, "r")
	filecopy = start.read()			#Open and read .gff files
	

	annolist = []
	annolist = filecopy.split("\n")		#split to a list of annotation strings...

	for k in range(len(annolist)):

		annolist[k] = annolist[k].split("\t")	#... which are split to sublists of annotation features

	diction = {
	"Sequence Reference : ": [],
	"Source : ": [],
	"Feature : ": [],
	"Start : ": [],
	"Stop : ": [],
	"Score : ": [],
	"Strand : ": [],
	"Phase : ": [],
	"Group : ": []
	}

	keynames = ["Sequence Reference : ","Source : ","Feature : ","Start : ","Stop : ","Score : ","Strand : ","Phase : ","Group : "]

	for i in range(len(annolist)):
		for m in range(len(annolist[i])):
		
			diction[keynames[m]].append(annolist[i][m])		#all annotations save to dictionary for safe-keeping

	if diction["Sequence Reference : "][len(diction["Sequence Reference : "])-1] == '':
		diction["Sequence Reference : "].remove(diction["Sequence Reference : "][len(diction["Sequence Reference : "])-1])
										#Removing unwanted emptyline at bottom of some .gff files

	print("File Loaded: %i annotations successfully loaded from file '%s':\n" %(len(diction["Sequence Reference : "]),GFF))
	
	aps = []


	for l in range(len(diction["Sequence Reference : "])):

		aps.append(diction["Sequence Reference : "][l])	

	aps2 = [change.lower() for change in aps]	#for OOP, ID alphabetic characters stored as lowercase, so may be used as object values
							#aps is list of all seq annotations
	apsset = []
	apsset = list(set(aps2))			

	for it in range(len(apsset)):			#appset is list of total seqs for which there are annotations...

		print("%s = %i annotations loaded.\n" %(apsset[it].upper(),int(aps2.count(apsset[it]))))#... thus list annotations per seq ID
	
	
	for g in range(len(aps2)):
		anno = Annotate(diction["Sequence Reference : "][g], diction["Source : "][g], diction["Feature : "][g], diction["Start : "][g], diction["Stop : "][g], diction["Score : "][g], diction["Strand : "][g], diction["Phase : "][g], diction["Group : "][g])
		alist.append(anno)


							#newly loaded annotations, stored to class "Annotate"












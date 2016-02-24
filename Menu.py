import menu_mod
import fastaloader
import gffloader
#First use of the menu
qq = 0
tt = 0
op = menu_mod.options(input("\nFASTA and GFF analyser\n================================================================\n1: Load a FASTA File (F)\n2: Load a GFF File (G)\n3: Explore annotations (A)\n4: Create annotations (C)\n5: Export GFF File (X)\n6: Quit (Q)\n================================================================\nStatus: %i sequences and %i annotations loaded. \nSelect option : " %(qq, tt)))

#All subsequent returns to the menu
while op == "":
	for seq in fastaloader.slist:
			qq = qq + 1
	for anno in gffloader.alist:
			tt = tt + 1
	op = menu_mod.options(input("\nFASTA and GFF analyser\n================================================================\n1: Load a FASTA File (F)\n2: Load a GFF File (G)\n3: Explore annotations (A)\n4: Create annotations (C)\n5: Export GFF File (X)\n6: Quit (Q)\n================================================================\nStatus: %i sequences and %i annotations loaded. \nSelect option : " %(qq, tt)))

	
	
	


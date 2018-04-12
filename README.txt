------------------------------------------------------------------------------------------------------------------------------------------------
Annolyser | By Crystal-Leigh Clitheroe | 23 February 2016
------------------------------------------------------------------------------------------------------------------------------------------------
Welcome to Annolyser_v01

This is a short terminal based program.

What it does, is parse and read-in sequence information from .fasta files and sequence annotations from .gff files and relates the the information by sequance identifiers. It allows the user to "explore" the annotations of interest and add new ones. The user can then write new .gff files for only the sequences of interest, along with the added annotations.

I plan to add a lot more functionality to this program, particularly with regard to inputting new sequences from raw Sanger and NGS .seq files. Then of course, provide an option to write the raw data into .fasta format and export new .fasta files.

Running the program in Linux, requires python3:

1.	Save and unarchive Annolyser<current_version>.tar.gz folder to directory of your choice.
2.	Move all gff and fasta files to be loaded into Annolyser folder.
3. 	Do NOT remove modules fastaloader.py, gffloader.py and menu_mod.py from Annolyser folder.
4.	In the commandline, within the Annolyser directory, start the program with command "python Menu.py"

Conditions on file formats: 

1.	Fasta and gff files must be of the sequence ID format i.e. ">XXX00000" not the ">XXX00000.0" or the ">gi:...|...|..." format. Am currently working on including these and more modern/contemporary file formats
2.	Sequence ID in both fasta and gff files must consist only of alphanumeric characters, the first ID character, ALWAYS be alphabetical.
Note:	This conditions are due to the object value rules for Class input, probably could have been overcome using dictionaries or lists, am working on relaxing this constraint by using a dictionary or list.

Outputs:

1.	Only .gff format files are outputted, but the user must stipulate <FILENAME>.gff when exporting to file path.
2.	The default output directory is Annolyser, where the program is running.

-----------------------------------------------------------------------------------------------------------------------------------------------

General Notes:

Bugs and issues:

1. There are no cushy safetynets, so if  a filename or sequence ID is entered incorrectly, the program will just return trace errors and end, and the user will have to start again.

Note: There are carefully designed example files fastaex.fasta and gffex.gff included in the MenuGuy folder, that are examples of the input file formats that are supported by this program, and have taken into account and present the subtle problems of the Explore and Create Annotations sections (eg, formatting of Sequences around START and STOP features).

Acknowledgements:
Many thanks to Gustavo Salazar, who debugged the some of the code in the fileloaders. 

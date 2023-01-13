# DDR-DOGGO
This repository holds python code to identify percentage of DDR dogs in a base dog's lineage.

To run this code, simply run the "findDDR(dogName= '', generationCount = 0)" function, with all necessary supporting functions:
  findDDR.py
  findParents.py
  isDDR.py
  isTooOld.py
  
There is a file called "MAIN.py" that simply imports the main recursive function, and calls the function.

Example call for running the program, and printing DDR-ness of a dog to console, simply run the findDDR() function with the PDB URL of the dog, and generation count parameter blank (this is used for recursive calling of the findDDR function and tracking the current generation):

print(findDDR('https://www.pedigreedatabase.com/german_shepherd_dog/dog.html?id=3117544-qui-vive-hektor-von-sentinelharts?_v=20211107093250'))

All dogs in the lineage will be printed to console, with their PDB URL (this can obviously be coded out, but since this function runs so slowly, it is a nice tracker of how far into the search you are going). There is also text output when a line is exhausted either via age limits ("exhausted a lin, no DDR dog found in XX generations") or via DDR dog being found in the lines ("Found a DDR dog line in Generation XX - Dog Name: {URL PRINTED FROM PDB}")

Dogs that are "not very DDR" will exhaust searching the lineage tree until the age of the dog is above whatever the threshhold is set to in "isTooOld.py". In the below example, the year threshold is 1970. This value must be manually set in two different locations in the isTooOld.py script. If the search is taking too long (because DDR dogs are either not present, or are present very distant in the family tree, you can increase the threshold to a more recent year, however you will potentially lose some DDR precentage if the script exits searching for a DDR dog before a DDR dog was found.

if int(yearBorn) < 1970:   <--- Set "1970" to whatever value you would like to set as your "exit" condition for searching back in a lineage for a DDR dog. This must be changed in TWO places in the isTooOld.py script. To be 100% certain of a dog's DDR-ness, you must search back to 1949 = creation of the DDR in germany, which is anywhere from 130,000 to 1,000,000 dogs searched in pedigree database, which is not feasible (you would probably be blacklisted from PDB). Typically, i found fairly accurate results running 1980 or 1970 as a threshold date, which only requires parsing typically 4k-ish dogs, depending on the age of the dogs in the lines.

Depending on the information contained in PDB, the process may fail. I have actually caught issues with lineage in PDB because of this program entering endless loops (a grand-child was the parent of the grandparents in another line- impossible scenario). If you find issues with lines, you can email PDB and they will fix the lines. You can also comment on the dog in issue and usually the "owner" will fix it (or if there is no owner, you can fix it). Sometimes it was just a mistyped dog's name when someone entered a new dog's parents into PDB.

the last line in the script printed to console wil be a decimal number. Multiply by 100, and that is the percent, i.e.:
0.5 (in last line of script after completion) = 50% DDR dog


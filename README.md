# Python Renamer
This script changes file names in bulk. It was one of my first python scripts.

I created it to solve a problem with files names auto generated in Nikon folders after 9999 photos taken with my D90, but this can be used to change or remove arbitrary characters or strings that repeat themselves in files inside a folder.

## How to use:

1 - Run this script as a stand-alone (terminal > python python-renamer.py) inside a root folder of the files you want to perform the name changing
2 - Type the character or string you want to change
3 - Type in which position you want it to change (i.e:. if you choose "a" in step 2, now you choose which "a" should be changed, the first one the script finds, the second one, etc)
4 - Type what should the script change the character/string to

Every step is printed in terminal with step by step questions, including result in changes.

OBS 1: In some systems the ANSI color at the end might persist after the script runs. Be sure to remove them from the last print statement, as they may change the instantiated font colors of your terminal

OBS 2: This works with both python 2 and python 3 (no need to adjust the code)

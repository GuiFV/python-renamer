# -*- coding: utf-8 -*-
# o primeiro programa a gente nunca esquece...
from __future__ import print_function
import os
import sys

def main():

    def user_input(screen_text):
        # Support for input string on python 2 and python 3
        if sys.version_info[0] > 2:
            return input(screen_text)
        else:
            return raw_input(screen_text)

    get_path =  os.getcwd()
    position = 0

    print("\nFolders found:\n-","- " * 39) 

    for root, dirs, files in os.walk(get_path):
        position += 1
        print(position, root)

    print("- " * 40)

    while True:

        subfolder_name = user_input("Type subfolder name. Press ENTER to select current folder (first on list): ")

        if (len(subfolder_name) < 1): 
            folder = os.getcwd()
        else:
            folder = f'{os.getcwd()}/{subfolder_name}'
        try:
            os.listdir(folder)
            print("- "*40, "\n" "Selected folder is: ", folder, "\n\nFiles found:\n")
            for file in os.listdir(folder):
                print(file)
            print('\n')
            break
        except:
            print("\n\nInvalid name.\n\n")
            continue
            
    what_to_cut = user_input("What character or string in the file name should I cut? ")

    while True:
        try:
            start_cut_position = int(user_input("Enter which character/string occurrence will be replaced (1 = 1st, 2 = 2nd, etc.) "))
            break
        except:
            print("\n\nInvalid input.\n\n")
            continue

    replace_for = user_input("Replace character/string with following character or string: ")

    content_folder = os.listdir(folder)

    for content_unit in content_folder:
        folder_cut = content_unit.find(what_to_cut, start_cut_position)
        replace_content = content_unit.replace(what_to_cut,replace_for,1)
        old = folder+"/"+content_unit
        new = folder+"/"+replace_content
        print("\033[0;34m OLD:","\033[37;0m",content_unit,"\033[0;32m NEW:","\033[37;0m",replace_content) #ANSI colors
        os.rename(old, new)

if __name__ == "__main__":
    main()

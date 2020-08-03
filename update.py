import os

# The Main function of the moudlue.
# Can Update String in one file or run on all files in folders and Update a string inside.


def Update(File_Name, StringToBeUpdated, New_Updateted_String):

    print("Update Script Activated:\n")

    # Test for which operation: change on file or running on all files.
    operation = File_Name.find('*')

    # Case Update a string in one file
    if(operation == -1):

        # check if there is a file with this name in the folder.
        file_located = os.path.isfile(File_Name)

        if(file_located == False):
            print("File not Found.\n")
            exit()

        # if file located or the target is to run and Update string in all files
        ChangeSingleFile(File_Name, StringToBeUpdated, New_Updateted_String)

    # if file located or the target is to run and Update string in all files
    else:
        RunOnAllFile(StringToBeUpdated, New_Updateted_String)


def RunOnAllFile(StringToBeUpdated, New_Updateted_String):
    print("RunOnAllFile Function Activated.\n")
    for filename in os.listdir('.'):
        if(filename.lower().endswith('.html')):
            ChangeSingleFile(filename, StringToBeUpdated, New_Updateted_String)


def ChangeSingleFile(file_name, StringToBeUpdated, New_Updateted_String):
    print("ChangeSingleFile Function Activated on {}.\n".format(file_name))
    test_if_string_exists_and_Update(
        file_name, StringToBeUpdated, New_Updateted_String)


def test_if_string_exists_and_Update(file_name, StringToBeDelted, New_Updateted_String):

    does_string_exsists = False

    print("Test if string exsists:\n")

    with open(file_name) as target_file:
        if StringToBeDelted in target_file.read():
            print("string_exsists.\n")
            does_string_exsists = True

    if(does_string_exsists):
        # read input file
        fin = open(file_name, "rt")
        # read file contents to string
        data = fin.read()
        # replace all occurrences of the required string
        data = data.replace(StringToBeDelted, New_Updateted_String)
        # close the input file
        fin.close()
        # open the input file in write mode
        fin = open(file_name, "wt")
        # overrite the input file with the resulting data
        fin.write(data)
        # close the file
        fin.close()
        print("Text Updated.\n")

    else:
        print("Text does not exsist in file, program exit.\n")
        exit()


if __name__ == "__main__":

    # input("Enter file name to be Updated or press * for whole files in folder:")
    File_Name = "*"
    # input("Enter the string you want to Update:")
    StringToBeDelted = '''<form action="/search" class="search">
     <fieldset>
      <legend>
       חיפוש באתר
      </legend>
      <input name="q" type="text" value=""/>
      <input type="submit" value=""/>
     </fieldset>
    </form>'''
    # input("Enter the new string:")
    New_Updateted_String = ''' <!--
    <form action="/search" class="search">
     <fieldset>
      <legend>
       חיפוש באתר
      </legend>
      <input name="q" type="text" value=""/>
      <input type="submit" value=""/>
     </fieldset>
    </form>
    -->
    '''

    Update(File_Name, StringToBeDelted, New_Updateted_String)


"""

******Target 1: delete the facebook/Google/ Twitter baget******

'''<div class="share">
     <a class="f" href="http://www.facebook.com/profile.php?id=195611067175611" rel="external">
      Facebook
     </a>
     <a class="g" href="https://plus.google.com/u/0/108827267783947349583?rel=author" rel="author">
      Google Plus
     </a>
     <a class="t" href="http://twitter.com/#!/nadlandeal/" rel="external">
      Twitter
     </a>
</div>'''

******Target 2: delete the search field******

'''<form action="/search" class="search">
     <fieldset>
      <legend>
       חיפוש באתר
      </legend>
      <input name="q" type="text" value=""/>
      <input type="submit" value=""/>
     </fieldset>
    </form>


'''

----Target 3: Delete הצעות אטרקטיביות baget----

----Target 4: Delte סמסייט baget----

----Target 4: Delte  hiden frame Code----



----Target 5: Update all the Top menu Links----

----Target 6: Update all the Right menu Links----


"""

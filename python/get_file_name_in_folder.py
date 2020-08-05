"""

what this moudlue should do:

1.run on all html file in the folder.
2.if it is an html file open it.
3.search  inside the file that open and replace "file_name" -> "file_name.html"


"""
def change_links_inside_file(file_name,origan_string,new_string):
    # read input file
    fin = open(file_name, "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    #data = data.replace(file_name, file_name+".html")
    data = data.replace(origan_string,new_string)
    
    # close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file_name, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    print("change_links_inside_file activated on in {}.\n\n\n".format(file_name))


if __name__ == "__main__":

    

    
    import glob, os
    #os.chdir(".")
    for file in glob.glob("*.html"):
        print("working on {} \n".format(file))
        #this is the .html string
        base_string = str(file)
       
        enterded_string = "href=\'" + base_string + "\'"
        print("The string that will be insert: {} \n".format(enterded_string))

        #this is the sting i need to search
        searched_string = "href=\""+ base_string.replace(".html","") +'\"'
        print("The string that we are searching: {} \n".format(searched_string))

        #print(original + "\n")
        #print("The string that will be replaced")
        #change_links_inside_file(file)
        
        
        
        change_links_inside_file(file, searched_string, enterded_string)

    

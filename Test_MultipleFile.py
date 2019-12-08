import os,glob
folder_path = 'testdir'
str_search = "error_field"
for filename in glob.glob(os.path.join(folder_path, '*.log')):
  with open(filename, 'r') as f:
    text = f.readlines()

    if(text.__contains__(str_search)):
        print("The",filename,"contains the String",str_search)
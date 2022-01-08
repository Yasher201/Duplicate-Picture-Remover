import hashlib, os

def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return md5(f.read()).hexdigest()

#Find your directory and paste it in os.chdir()
directoryPath = "C:\\Users\\Yasher\\Desktop\\pics"
file_list = os.listdir(directoryPath)


duplicates = []
hash_keys = dict()

  
#Set directory where your files are located
for index, filename in enumerate(os.listdir(directoryPath)):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash] = index
        else:
        	duplicates.append((index,hash_keys[filehash]))

#This automatically deletes the duplicate file
for index in duplicates:
	os.remove(file_list[index[0]])


#This is just an extra function made if you want to rename all the files.
#Rename the pictures as -- Picture 1, Picture 2, Picture 3, etc.

def renameFiles():
	number = 1
	for fileName in os.listdir(directory):
		newFileName = "Picture " + str(number)+'.JPG'
		oldDestination = directory + "\\"+fileName
		newDestination = directory + "\\"+newFileName
		os.rename(oldDestination, newDestination)

		number += 1

# ===============================================================

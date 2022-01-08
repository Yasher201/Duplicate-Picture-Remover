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

def histogram(image):
	tonal_values = []
	range_list = list(range(256))
	for i in range(len(image)):
		for j in image[i]:
			tonal_values.append(j)
	for x in range(len(range_list)):
		range_list[x] = 0
	for y in tonal_values:
		range_list[y] += 1
	return range_list

def flip(image, orientation):
    if orientation == 'horizontal':
        for i in range((len(image))):
            for j in range(int(len(image[i])/2)):
                Value = image[i][j]
                image[i][j] = image[i][-j-1]
                image[i][-j-1] = Value
    else:
        for i in range(int(len(image)/2)):
            temp_list = image[i]
            image[i] = image[-i-1]
            image[-i-1] = temp_list

def rotate(image):
    copy_list = []

    for i in range(len(image)):
        copy_list.append([])
        for j in range(len(image[i])):
            copy_list[i].append(image[i][j]) 

    for row in range(len(copy_list)):
        for col in range(len(copy_list)):
            image[col][len(copy_list)-1-row] = copy_list[row][col]
    return None

def crop(image, origin, height, width):
    newImage = []
    for i in range(origin[0], origin[0]+height):
        newImage.append([])
        for j in range(origin[1], origin[1]+width):
            newImage[i-origin[0]].append(image[i][j])
    return newImage


def color2gray(image):
    grayScale = []

    for i in range(len(image)):
        grayScale.append([])
        for j in range(len(image[i])):
            total = 0
            for k in range(len(image[i][j])):
                total += image[i][j][k]
            total = int(total / len(image[i][j]))
            grayScale[i].append(total)
    return grayScale

def extract_layer(image, color):
    extracted = []

    color_index = 0
    if color == 'green':
        color_index = 1
    if color == 'blue':
        color_index = 2

    for i in range(len(image)):
        extracted.append([])
        for j in range(len(image[i])):
            extracted[i].append(image[i][j][color_index])

    return extracted

def scale(image, factor):
    scaleList = []
    if factor >= 1:
        for i in range(len(image)):
            listy = []
            for j in range(len(image[i])):
                for k in range(factor):
                    listy.append(image[i][j])
            for k in range(factor):
                scaleList.append(listy)
    elif factor <= -1:
        for i in range (0, len(image), -1 * factor):
            listy = [] 
            for j in range (0, len(image[i]), -1* factor):
                listy.append(image[i][j])
                scaleList.append(listy)
    for i in range (len(image)):
        image.pop()
    for i in range (len(scaleList)):
        image.append(scaleList[i])
    return None

def compress(image):
	new_list = []
	for i in range(len(image)):
		value = 0
		trial = 0
		empty_row = []
		for j in range(len(image[i])):
			if image[i][j] < 128:
				new_val = 0
			if image[i][j] >= 128:
				new_val = 1
			if new_val == value:
				trial += 1
			if new_val != value:
				empty_row.append(trial)
				value = new_val
				trial = 1
		empty_row.append(trial)
		new_list.append(empty_row)
	return new_list

def median_filter(image):
	final = []
	num_rows = len(image)
	num_cols = len(image[0])
	for rows in range(num_rows-2):
		empty_list = []
		for col in range(num_cols-2):
			new_list = []
			for i in range(3):
				for x in range(3):
					new_list.append(image[rows+i][col+x])
			new_list.sort()
			empty_list.append(new_list[4])
		final.append(empty_list)
	image = final
	return image
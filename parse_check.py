import csv


card_images_folder_names = [] 
with open('card_images_folder.csv', 'r') as f: 
	 reader = csv.reader(f)
	 for row in reader: 
	 	card_images_folder_names.append(row[0])


print(card_images_folder_names)


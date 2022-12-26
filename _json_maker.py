#makes json from dataset
import json

train_file = input("Enter the path of the training file: ")
wave_clips = input("Enter the path of the folder containing the .wav files: ")
json_out = input("Enter the path of the folder where you want to save the json file: ")

clips_list = []
count = 0
with open(train_file, 'r', encoding='utf8', newline='', errors='replace') as f:
    for line in f:
        file_name = line.split('\t')[1].strip()
        clips_list.append(file_name)
        count+=1
        
print("Total number of files in the training file: ", count)


#makes json from dataset
import json
import os

# train_file = input("Enter the path of the training file: ")
# wave_clips = input("Enter the path of the folder containing the .wav files: ")
# json_out = input("Enter the path of the folder where you want to save the json file: ")
train_file = "/home/jarvis/cv-corpus-12.0-2022-12-07/en/validated.tsv"
# wave_clips_1 = "/media/jarvis/WD1/wave_audio_dataset_p1"
# wave_clips_2 = "/media/jarvis/WD2/wave_audio_dataset_p2"
mp3_clips_path = "/home/jarvis/cv-corpus-12.0-2022-12-07/en/clips"
json_out = "/home/jarvis/json_model_train_mp3.json"

with open(json_out, 'w') as f:
    f.write('')

clips_list = []
sentence_list = []
count = 0
with open(train_file, 'r', encoding='utf8', newline='', errors='replace') as f:
    for line in f:
        file_name = line.split('\t')[1].strip()
        clips_list.append(file_name)

        sentence = line.split('\t')[2].strip()
        sentence_list.append(sentence)
        count+=1
        
print("Total number of files in the training file: ", count)



with open(json_out, 'a') as f:
    for file, sentence in zip(clips_list, sentence_list):
        # if file.endswith('mp3'):
        #     file = file.replace('.mp3', '.wav')
        
        if os.path.exists(mp3_clips_path+'/'+file):
            d = {'key': mp3_clips_path+'/'+file, 'text': sentence}
            x = json.dumps(d)
            f.write(x)
            f.write('\n')
        # elif os.path.exists(wave_clips_2+'/'+file):
        #     d = {'key': wave_clips_2+'/'+file, 'text': sentence}
        #     x = json.dumps(d)
        #     f.write(x)
        #     f.write('\n')
        else:
            print("File not found: ", file)
        
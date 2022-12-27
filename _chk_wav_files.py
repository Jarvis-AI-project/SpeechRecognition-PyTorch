import os

train_file = r"C:\cv-corpus-12.0-2022-12-07\en\validated.tsv"
wav_files = r"E:\wav_audio_dataset"

with open('remaining_conversion_files.txt', 'w') as f:
    f.write('')
f.close()

train_files=[]
count_train =0
with open(train_file, 'r', encoding='utf8', newline='', errors='replace') as f:
    for line in f:
        file_name = line.split('\t')[1].strip()
        train_files.append(file_name)
        count_train+=1
        
print('Files Requred for Training: ', count_train)

lst_wav = os.listdir(wav_files)
print('Files present in folder: ', len(lst_wav))

print('Files missing: ', count_train-len(lst_wav))

x=str(input("Do you want to create a checkpoint? (y/n): "))
if count_train-len(lst_wav) > 0 and x == 'y':
    for i in train_files:
        if i not in lst_wav:
            with open('remaining_conversion_files.txt', 'a') as f:
                f.write(i)
                f.write('\n')
f.close()
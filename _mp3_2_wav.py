from pydub import AudioSegment
# import multiprocessing as mp
import threading as th
import os
import sys
from time import sleep
from time import time

# max_processes = 100
max_threads = 400
current_time = time()

# max_threads = int(input("Enter the number of max threads: "))
# folder_path = str(input("Enter the cv-corpus folder path: "))
# train_file = str(input("Enter the training file path: "))
# wave_out_path = str(input("Enter the output folder path: "))
max_threads = 300
folder_path = r'G:\cv-corpus-12.0-2022-12-07\en'
train_file = r"G:\cv-corpus-12.0-2022-12-07\en\validated.tsv"
wave_out_path = r"C:\wave-out"

lst_files=[]
count_train =0
with open(train_file, 'r', encoding='utf8', newline='', errors='replace') as f:
    for line in f:
        file_name = line.split('\t')[1].strip()
        lst_files.append(file_name)
        count_train+=1
count_mp3 = 0
index = 1

# make wav_audio_dataset folder if it doesn't exist
if not os.path.exists(wave_out_path):
    print("Creating wav_audio_dataset folder")
    os.mkdir(wave_out_path)
else:
    print("wav_audio_dataset folder already exists")

for i in lst_files:
    if i.endswith('.mp3'):
        count_mp3 += 1
    else:
        continue
print('Total number of files in the folder: ', len(os.listdir(folder_path+'//'+'clips')))
print('Total number of files in the training file: ', count_train)
print(".mp3 files found: ", count_mp3)


cont = input("Do you want to continue? (y/n): ")
if cont == 'y':
    print("Converting files to wav")
else:
    sys.exit(1)
# def temp():
#     r = 9542358932693*9295239632
#     return r

def write_error_log(log):
    with open("error_files.txt", 'a') as f:
        f.write(log)
        f.write('\n')

def convert(mp3_path, wave_path):
    try:
        # print(mp3_path)
        # print(wave_path)
        mp3 = AudioSegment.from_mp3(mp3_path)
        mp3.export(wave_path, format="wav")
    except Exception as e:
        print(e)
        # print("OS Error")
        print("Error in converting file: ", mp3_path)
        while True:
            try:
                write_error_log(mp3_path +' | ' +  e)
                break
            except Exception as e:
                continue
                
        # sys.exit(1)


if __name__ == '__main__':
    # print('No of .mp3 files found: ', count_mp3)
    for mp3 in lst_files:
        if mp3.endswith('.mp3'):
            mp3_path = folder_path + '\\clips\\' + mp3
            wave_path = wave_out_path + '\\' + mp3.replace('.mp3', '.wav')
            print("Converting File: " + str(index) + "/" + str(count_mp3) + " to wav" + ' | ' +
                  'Time Passed: ', "'{}' hour '{}' min '{}' second".format(round(((time() - current_time)//3600), 1), round((((time() - current_time)%3600)/60)), round(((time()-current_time) % 60), 1)) + ' | ' +
                  'Time Remaining: ', "'{}' hour '{}' min '{}' second".format(round((((time() - current_time) * (count_mp3 - index) / index)//3600), 1), round(((((time() - current_time) * (count_mp3 - index) / index)%3600)/60)), round((((time() - current_time) * (count_mp3 - index) / index) % 60), 1)), end='\r')
            # print('\r\r\r')
            # print('Time passed: ', time() - current_time, 'seconds', end='\r')
            index += 1
            # sleep(.001)

            while True:
                # mp.Process(target=temp).start()
                # th.Thread(target=temp).start()

                # print('{} processes are running',len(mp.active_children()))

                # if len(mp.active_children())<max_processes:
                # print(len(th.enumerate()))
                if len(th.enumerate()) < max_threads:
                    # print(mp.active_children())
                    # p = mp.Process(target=convert, args=(mp3_path, wave_path))
                    th.Thread(target=convert, args=(
                        mp3_path, wave_path)).start()
                    break
                # else:
                #     sleep(1)
                    # print('-'*50, end = '\r')
                    # print('\n')
                    # print('Waiting for a thread to finish...', end='\r')
                    # print('Waiting for a process to finish...')
                    # print('Active processes: ', mp.active_children())
                    # print('Active threads: ', len(th.enumerate()), end='\n\n')
                    # print(mp3)
                    # print('-'*50, end = '\r')

        else:
            print("'{}' not a mp3 file".format(mp3))

    print("Congratulations '{}' files have been successfully converted to wave in '{}' seconds".format(
        index-1, round(time() - current_time, 2)))
    print('Conversion Speed: "{}" files per second'.format(
        round((index-1)/(time() - current_time))))

    # remove wav_audio_dataset folder if it exists
    if len(th.enumerate()) > 0:
        print('Waiting for threads to finish', end='\r')
        sleep(1)
    os.system('rmdir /s /q "{}"'.format(wave_out_path))
    print('wav_audio_dataset folder removed')

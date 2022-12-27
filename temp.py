# # import json

# # #open json file
# # clips_list = {
# #     "clips": 'clip_name',
# #     "text": 'text'
# # }

# # with open('temp.json', 'w') as f:
# #     l= json.dumps(clips_list)
# #     f.write(l+'\n')
# #     l= json.dumps(clips_list)
# #     f.write(l+'\n')


# import subprocess
# import os
# # import tensorflow as tf

# # Set the input and output filenames
# input_filename = 'common_voice_en_1.mp3'
# output_filename = 'output.wav'


# # Set the path to the ffmpeg executable
# # ffmpeg_path = '/path/to/ffmpeg'

# # Set the input and output filenames
# # input_filename = 'input.mp3'
# # output_filename = 'output.wav'

# # Build the ffmpeg command
# # command = 'ffmpeg'+ '--hwaccel cuda'+ '-i',
# #            input_filename '-c:a', 'pcm_s16le', output_filename

# command = "ffmpeg -hwaccel opencl -i common_voice_en_1.mp3 -c:a pcm_s16le output.wav"

# # Run the command
# while True:
#     subprocess.run(command)
#     os.remove(output_filename)
    
# # import pydub
# # import os
# # while True:
# #     pydub.ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
# #     l = pydub.AudioSegment.from_mp3(input_filename)
# #     l.export(output_filename, format="wav")
#     # os.remove(output_filename)
from dotenv import load_dotenv
import os
print(os.environ.get('MAX_THREADS'))

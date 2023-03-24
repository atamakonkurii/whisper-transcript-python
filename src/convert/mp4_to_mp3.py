import ffmpeg
import os

def find_first_mp4_file(directory):
    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            return os.path.join(directory, file)
    return None

input_directory = "./input_movie"
input_file = find_first_mp4_file(input_directory)

if input_file is None:
    print(f"No MP4 files found in {input_directory}")
    sys.exit(1)

# 入力 
stream = ffmpeg.input(input_file) 
# 出力 
# stream = ffmpeg.output(stream, "./output/mp3/voice.mp3", ab="64k") 
stream = ffmpeg.output(stream, "./output/mp3/voice.mp3") 
# 実行 
ffmpeg.run(stream)
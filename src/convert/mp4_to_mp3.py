import ffmpeg 

# 入力 
stream = ffmpeg.input("./input_movie/movie.mp4") 
# 出力 
stream = ffmpeg.output(stream, "./output/mp3/voice.mp3") 
# 実行 
ffmpeg.run(stream)
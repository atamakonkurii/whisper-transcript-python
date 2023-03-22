import os
import openai

from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()
# apikeyを渡す
openai.api_key = os.environ["OPENAI_API_KEY"]

# audioファイル読み込み
audio_file= open("./audio_file/test.mp3", "rb")

# whisper-1モデルで音声認識⇨Japanese
transcriptJapanese = openai.Audio.transcribe(model="whisper-1", 
                                     file=audio_file,
                                     language="ja",
                                     temperature=0,
                                     response_format="srt",)

with open('./output/transcriptJapanese.srt', 'w') as f:
  print(transcriptJapanese, file=f)



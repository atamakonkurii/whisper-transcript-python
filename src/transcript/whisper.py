import os
import openai
from dotenv import load_dotenv

def transcript(input_audio_file, output_file_name, api_key):
  # apikeyを渡す
  openai.api_key = api_key

  # audioファイル読み込み
  audio_file= open(input_audio_file, "rb")

  # whisper-1モデルで音声認識⇨Japanese
  transcriptJapanese = openai.Audio.transcribe(model="whisper-1", 
                                              file=audio_file,
                                              language="ja",
                                              temperature=0,
                                              response_format="srt",)

  with open(output_file_name, 'w') as f:
    print(transcriptJapanese, file=f)

# 環境変数を読み込む
load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
input_audio_file = "./input/mp3/voice.mp3"  # 文字起こしをするmp3ファイルの名前
output_file_name = "./output/srt/transcriptJapanese.srt"  # 生成後のSRTファイルの名前

transcript(input_audio_file, output_file_name, api_key)
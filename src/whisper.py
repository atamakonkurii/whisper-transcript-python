import os
import openai

from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()
# apikeyを渡す
openai.api_key = os.environ["OPENAI_API_KEY"]

# audioファイル読み込み
audio_file= open("./audio_file/test.mp3", "rb")

# 
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript.text)
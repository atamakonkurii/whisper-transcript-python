import sys
import os
import shutil
from pydub import AudioSegment
from pathlib import Path

# src ディレクトリの絶対パスを取得
src_dir = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# sys.path に絶対パスを追加
sys.path.insert(0, str(src_dir))

# global_value.py をインポート
import global_value as g

# 入力ファイル名と出力ディレクトリ名
input_file = "./output/mp3/voice.mp3"
output_dir = "./output/mp3/split"

# 出力ディレクトリが存在する場合は削除してから再作成
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

# MP3ファイルを読み込み
audio = AudioSegment.from_mp3(input_file)

# 分割する時間間隔をミリ秒単位で設定 
interval = g.interval

# 分割処理
for i, chunk in enumerate(audio[::interval]):
    start_time = i * interval
    end_time = start_time + interval
    output_file = os.path.join(output_dir, f"chunk_{i+1}.mp3")
    chunk.export(output_file, format="mp3")

print("分割が完了しました。")
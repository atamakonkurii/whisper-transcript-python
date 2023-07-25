import os
import re
import glob
import sys
from pathlib import Path

# src ディレクトリの絶対パスを取得
src_dir = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# sys.path に絶対パスを追加
sys.path.insert(0, str(src_dir))

# global_value.py をインポート
import global_value as g

# 入力ディレクトリと出力ファイル名
input_dir = "./docker_share/output/srt/japanese"
output_file = "./docker_share/output/srt/combined_japan.srt"

# SRTファイルのリストを取得
srt_files = glob.glob(os.path.join(input_dir, '*.srt'))
# ファイルの作成時刻でソート
# sorted_srt_files = sorted(srt_files, key=os.path.getctime)

# ファイル名でソート
sorted_srt_files = sorted(srt_files)

# 分割されたSRTファイルを組み合わせる
combined_srt = ""
start_time_offset = 0
subtitle_index_offset = 0


def convert_timestamp_to_ms(timestamp):
    hours, minutes, seconds_milliseconds = timestamp.split(":")
    seconds, milliseconds = seconds_milliseconds.split(",")
    return int(hours) * 3600000 + int(minutes) * 60000 + int(seconds) * 1000 + int(milliseconds)

def convert_ms_to_timestamp(milliseconds):
    hours = int(milliseconds / 3600000)
    minutes = int((milliseconds % 3600000) / 60000)
    seconds = int((milliseconds % 60000) / 1000)
    ms = milliseconds % 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{ms:03d}"

for srt_file in sorted_srt_files:
    with open(srt_file, "r") as f:
        lines = f.readlines()

    # 余分な空行を削除
    lines = [line for line in lines if line.strip()]

    for i in range(len(lines)):
        line = lines[i]

        # タイムスタンプ行を探す
        if "-->" in line:
            start_time, end_time = line.strip().split(" --> ")

            # タイムスタンプをミリ秒単位に変換
            start_time_ms = convert_timestamp_to_ms(start_time)
            end_time_ms = convert_timestamp_to_ms(end_time)

            # オフセットを適用
            start_time_ms += start_time_offset
            end_time_ms += start_time_offset

            # オフセットを適用したタイムスタンプが次のファイルの開始時間を超えていたら修正
            if start_time_ms > g.interval + start_time_offset:
                start_time_ms = g.interval + start_time_offset

            if end_time_ms > g.interval + start_time_offset:
                end_time_ms = g.interval + start_time_offset

            # 新しいタイムスタンプを作成
            new_start_time = convert_ms_to_timestamp(start_time_ms)
            new_end_time = convert_ms_to_timestamp(end_time_ms)

            # タイムスタンプ行を置き換え
            lines[i] = f"{new_start_time} --> {new_end_time}\n"
        elif re.match(r"^\d+$", line.strip()):
            # インデックス行を見つけてオフセットを適用
            current_index = int(line.strip())
            new_index = current_index + subtitle_index_offset
            lines[i] = f"{new_index}\n"
        else:
            lines[i] = f"{line}\n"

    # オフセットを更新
    start_time_offset += g.interval

    # 最後のインデックスを取得して、インデックスオフセットを更新
    last_index_line = [line for line in lines if re.match(r"^\d+$", line.strip())][-1]
    last_index = int(last_index_line.strip())
    subtitle_index_offset = last_index

    # 組み合わせたSRTファイルに追加
    combined_srt += "".join(lines)

# 組み合わせたSRTファイルを保存
with open(output_file, "w") as f:
    f.write(combined_srt.strip())

print("SRTファイルの組み合わせが完了しました。")

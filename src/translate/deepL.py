import os
import requests
import json
import re
from dotenv import load_dotenv

# transcriptJapanese.srtファイルをdeepLで翻訳
def translate_text(text, target_language, api_key):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": api_key,
        "text": text,
        "target_lang": target_language,
    }
    response = requests.post(url, data=data)
    result = json.loads(response.text)
    return result["translations"][0]["text"]

def translate_srt_file(input_file, output_file, target_language, api_key):
    with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
        for line in fin:
            if re.match("^\d+$", line.strip()) or re.match("^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$", line.strip()):
                fout.write(line)
            elif line.strip():
                translated_line = translate_text(line.strip(), target_language, api_key)
                fout.write(translated_line + "\n")
            else:
                fout.write("\n")

# 環境変数を読み込む
load_dotenv()

api_key = os.environ["DEEPL_API_KEY"]  # ここにDeepL APIキーを入力してください
input_file = "./docker_share/output/srt/combined_japan_fix.srt"  # 変換するSRTファイルの名前
output_file = "./docker_share/output/srt/combined_taiwanese_deepl.srt"  # 変換後のSRTファイルの名前
target_language = "ZH-HANT"  # 変換後の言語を指定してください

translate_srt_file(input_file, output_file, target_language, api_key)


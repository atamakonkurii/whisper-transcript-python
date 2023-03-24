import pysrt
from dotenv import load_dotenv
from google.cloud import translate_v2 as translate


# transcriptJapanese.srtファイルをGoogle Translateで翻訳
def translate_srt_file(input_file, output_file, source_language='ja', target_language='zh-TW'):
    # 字幕ファイルを読み込む
    subs = pysrt.open(input_file, encoding='utf-8')

    # 翻訳オブジェクトを作成
    translate_client = translate.Client()

    # 各字幕を翻訳
    for sub in subs:
        result = translate_client.translate(sub.text, 
                                            source_language=source_language, 
                                            target_language=target_language)
        translated_text = result['translatedText']
        sub.text = translated_text

    # 翻訳された字幕ファイルを保存
    subs.save(output_file, encoding='utf-8')

# 環境変数を読み込む
load_dotenv()

input_file = "./output/transcriptJapanese.srt"  # 変換するSRTファイルの名前
output_file = "./output/transcriptTaiwanese.srt"  # 変換後のSRTファイルの名前

translate_srt_file(input_file, output_file)

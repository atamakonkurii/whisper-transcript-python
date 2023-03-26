### このファイルは、SRTファイルをXMLファイルに変換するためのスクリプトです。
### AdobePremiere

import re

def srt_to_xml(input_file, output_file_name):
    # 字幕ファイルを読み込む
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    subtitles = re.findall(r'(\d+)\s+(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\s+([\s\S]*?)(?=\n\n\d+|\Z)', content)

    xml_output = "<subtitles>\n"
    for index, start, end, text in subtitles:
        xml_output += '  <subtitle start="{}" end="{}">{}</subtitle>\n'.format(start, end, text.strip().replace("\n", " "))
    xml_output += "</subtitles>"

    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write(xml_output)

    print(f"Converted {input_file} to {output_file_name}")

def main():
    input_japanese_file = "./output/srt/transcriptJapanese.srt"  # 変換するSRTファイルの名前
    input_taiwanese_file = "./output/srt/transcriptTaiwanese.srt"  # 変換するSRTファイルの名前
    output_japanese_file = "./output/xml/transcriptJapanese.xml"  # 出力するXMLファイルの名前
    output_taiwanese_file = "./output/xml/transcriptTaiwanese.xml"  # 出力するXMLファイルの名前

    srt_to_xml(input_japanese_file, output_japanese_file)
    srt_to_xml(input_taiwanese_file, output_taiwanese_file)

if __name__ == "__main__":
    main()
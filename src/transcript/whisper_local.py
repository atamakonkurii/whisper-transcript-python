import whisper

model = whisper.load_model("large-v2")
audio = model.transcribe("./output/mp3/split/chunk_1.mp3")

print(audio["text"])

# terminal
# whisper output/mp3/split/chunk_4.mp3 --model large --output_dir output/srt/japanese --output_format srt --fp16 False --language ja --initial_prompt "大阪旅行に近鉄の火の鳥に乗って行きます" 

# $ whisper --help 
# usage: whisper [-h] [--model {tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}] [--model_dir MODEL_DIR] [--device DEVICE] [--output_dir OUTPUT_DIR]
#                [--output_format {txt,vtt,srt,tsv,json,all}] [--verbose VERBOSE] [--task {transcribe,translate}]
#                [--language {af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba}]
#                [--temperature TEMPERATURE] [--best_of BEST_OF] [--beam_size BEAM_SIZE] [--patience PATIENCE] [--length_penalty LENGTH_PENALTY] [--suppress_tokens SUPPRESS_TOKENS]
#                [--initial_prompt INITIAL_PROMPT] [--condition_on_previous_text CONDITION_ON_PREVIOUS_TEXT] [--fp16 FP16] [--temperature_increment_on_fallback TEMPERATURE_INCREMENT_ON_FALLBACK]
#                [--compression_ratio_threshold COMPRESSION_RATIO_THRESHOLD] [--logprob_threshold LOGPROB_THRESHOLD] [--no_speech_threshold NO_SPEECH_THRESHOLD] [--word_timestamps WORD_TIMESTAMPS]
#                [--prepend_punctuations PREPEND_PUNCTUATIONS] [--append_punctuations APPEND_PUNCTUATIONS] [--threads THREADS]
#                audio [audio ...]

# positional arguments:
#   audio                 audio file(s) to transcribe

# options:
#   -h, --help            show this help message and exit
#   --model {tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}
#                         name of the Whisper model to use (default: small)
#   --model_dir MODEL_DIR
#                         the path to save model files; uses ~/.cache/whisper by default (default: None)
#   --device DEVICE       device to use for PyTorch inference (default: cpu)
#   --output_dir OUTPUT_DIR, -o OUTPUT_DIR
#                         directory to save the outputs (default: .)
#   --output_format {txt,vtt,srt,tsv,json,all}, -f {txt,vtt,srt,tsv,json,all}
#                         format of the output file; if not specified, all available formats will be produced (default: all)
#   --verbose VERBOSE     whether to print out the progress and debug messages (default: True)
#   --task {transcribe,translate}
#                         whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate') (default: transcribe)
#   --language {af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba}
#                         language spoken in the audio, specify None to perform language detection (default: None)
#   --temperature TEMPERATURE
#                         temperature to use for sampling (default: 0)
#   --best_of BEST_OF     number of candidates when sampling with non-zero temperature (default: 5)
#   --beam_size BEAM_SIZE
#                         number of beams in beam search, only applicable when temperature is zero (default: 5)
#   --patience PATIENCE   optional patience value to use in beam decoding, as in https://arxiv.org/abs/2204.05424, the default (1.0) is equivalent to conventional beam search (default: None)
#   --length_penalty LENGTH_PENALTY
#                         optional token length penalty coefficient (alpha) as in https://arxiv.org/abs/1609.08144, uses simple length normalization by default (default: None)
#   --suppress_tokens SUPPRESS_TOKENS
#                         comma-separated list of token ids to suppress during sampling; '-1' will suppress most special characters except common punctuations (default: -1)
#   --initial_prompt INITIAL_PROMPT
#                         optional text to provide as a prompt for the first window. (default: None)
#   --condition_on_previous_text CONDITION_ON_PREVIOUS_TEXT
#                         if True, provide the previous output of the model as a prompt for the next window; disabling may make the text inconsistent across windows, but the model becomes less prone to
#                         getting stuck in a failure loop (default: True)
#   --fp16 FP16           whether to perform inference in fp16; True by default (default: True)
#   --temperature_increment_on_fallback TEMPERATURE_INCREMENT_ON_FALLBACK
#                         temperature to increase when falling back when the decoding fails to meet either of the thresholds below (default: 0.2)
#   --compression_ratio_threshold COMPRESSION_RATIO_THRESHOLD
#                         if the gzip compression ratio is higher than this value, treat the decoding as failed (default: 2.4)
#   --logprob_threshold LOGPROB_THRESHOLD
#                         if the average log probability is lower than this value, treat the decoding as failed (default: -1.0)
#   --no_speech_threshold NO_SPEECH_THRESHOLD
#                         if the probability of the <|nospeech|> token is higher than this value AND the decoding has failed due to `logprob_threshold`, consider the segment as silence (default: 0.6)
#   --word_timestamps WORD_TIMESTAMPS
#                         (experimental) extract word-level timestamps and refine the results based on them (default: False)
#   --prepend_punctuations PREPEND_PUNCTUATIONS
#                         if word_timestamps is True, merge these punctuation symbols with the next word (default: "'“¿([{-)
#   --append_punctuations APPEND_PUNCTUATIONS
#                         if word_timestamps is True, merge these punctuation symbols with the previous word (default: "'.。,，!！?？:：”)]}、)
#   --threads THREADS     number of threads used by torch for CPU inference; supercedes MKL_NUM_THREADS/OMP_NUM_THREADS (default: 0)
# whisper-transcript-python
OpenAIのwisper apiを利用して、音声ファイルから字幕ファイル(*.srt)を生成する。
その際、日本語と繁体中国語のスクリプトが欲しいため、translate apiを利用して日本語から繁体中国語に翻訳をする。

Google Translate, DeepL, OpenAI gpt-3.5-turboの３種類を試して、Google Translateを利用することに決めた。

#### Google Translate
* 繁体中国語に翻訳可能
* 50万字まで無料([価格](https://cloud.google.com/translate/pricing?hl=ja))

#### DeepL
* 翻訳精度は高そう
* しかし、繁体中国語への翻訳不可
* 50万字まで無料([価格](https://support.deepl.com/hc/ja/articles/360020685720-DeepL-API-%E6%96%87%E5%AD%97%E6%95%B0%E3%81%AE%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%A8%E8%AB%8B%E6%B1%82#:~:text=DeepL%20API%20Pro%E3%81%A7%E3%81%AF%E3%80%81API,%E5%86%86%E3%81%A7%E7%AE%97%E5%87%BA%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82))

#### OpenAI gpt-3.5-turbo
* プロンプトとレスポンスを取り出すコードが下手すぎなのが原因だと思われるが、１行の日本語に対してレスポンスの行数が読めないので一旦見送り。
* $0.002 / 1K tokens([価格](https://openai.com/pricing))

#### Docker化
https://zenn.dev/atakon/scraps/723358fecce380

#### チートシート

```
docker-compose up -d
```

```
docker-compose exec python bash
```

```
./movie_to_srt.sh
```

```
./translate.sh
```

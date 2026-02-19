# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

MP4動画から日本語字幕（SRT形式）を生成し、繁体中国語に翻訳するPythonベースのパイプライン:
1. MP4動画をMP3音声ファイルに変換
2. 長い音声ファイルを5分間隔のチャンクに分割
3. OpenAI Whisper API（モデル: gpt-4o-transcribe）を使用して日本語字幕を生成
4. 分割されたSRTファイルを結合し、タイムスタンプを調整
5. Google Translate APIを使用して日本語字幕を繁体中国語（zh-TW）に翻訳

## 開発環境

### Docker セットアップ

```bash
# コンテナ起動（イメージがなければ作成）
docker-compose up -d

# コンテナに入る
docker-compose exec python bash

# 再ビルド
docker-compose build
docker-compose build --no-cache  # キャッシュなし

# コンテナを停止
docker-compose down
```

コンテナ名: `transcript-whisper`

### パイプラインの実行

**Dockerコンテナ内で実行:**

完全な文字起こしパイプライン（日本語動画 → 日本語SRT）:
```bash
cd /usr/src
./movie_to_srt.sh
```

このスクリプトは4つのステップを順次実行:
1. `python convert/mp4_to_mp3.py` - `docker_share/input_movie/`内の最初のMP4ファイルをMP3に変換
2. `python convert/split_mp3.py` - 音声を5分間隔のチャンクに分割（`global_value.py`で設定可能）
3. `python transcript/whisper_api.py` - 各チャンクをOpenAI Whisper APIで文字起こし
4. `python convert/combine_srt.py` - SRTファイルをタイムスタンプ調整して結合

翻訳パイプライン（日本語SRT → 繁体中国語SRT）:
```bash
./translate.sh
# 実行内容: python translate/googleTranslate.py
```

## アーキテクチャ

### パイプラインの流れ

```
MP4動画 (docker_share/input_movie/)
  → mp4_to_mp3.py → movie_audio.mp3
  → split_mp3.py → chunk_01.mp3, chunk_02.mp3, ... (5分間隔)
  → whisper_api.py → chunk_1.srt, chunk_2.srt, ... (日本語文字起こし)
  → combine_srt.py → combined_japan.srt (タイムスタンプ調整してマージ)
  → [combined_japan.srtを手動編集 → combined_japan_fix.srt]
  → googleTranslate.py → combined_taiwanese.srt (繁体中国語)
```

### ディレクトリ構成

```
src/
  convert/              # 音声・字幕フォーマット変換ユーティリティ
    mp4_to_mp3.py       # ffmpeg-pythonで音声抽出
    split_mp3.py        # pydubで時間間隔ごとに分割
    combine_srt.py      # 分割されたSRTファイルを結合、インデックスとタイムスタンプを調整
  transcript/           # 音声文字起こし
    whisper_api.py      # OpenAI Whisper API連携（gpt-4o-transcribeモデル）
  translate/            # 翻訳サービス
    googleTranslate.py  # Google Translate API（繁体中国語対応のため選定）
  global_value.py       # 共有設定（音声分割間隔: 5分）

docker_share/           # データ交換用マウントボリューム
  input_movie/          # 元のMP4ファイルをここに配置
  output/
    mp3/                # 生成された音声ファイル
      split/            # 分割された音声チャンク
    srt/                # 生成された字幕ファイル
      japanese/         # チャンクごとの日本語SRTファイル
```

### 主要な設定

**音声分割間隔** (`src/global_value.py`):
- 現在は5分（300,000ミリ秒）に設定
- `split_mp3.py`と`combine_srt.py`の両方で使用され、タイムスタンプの整合性を保つ
- 必要に応じて10分または15分に変更可能

**APIキー** (`.env`ファイル):
- `OPENAI_API_KEY` - Whisper文字起こしに必須
- `DEEPL_API_KEY` - 利用可能だが未使用（DeepLは繁体中国語非対応）
- Google Translateは`key.json`のサービスアカウント認証情報を使用（Dockerにマウント）

**Whisper文字起こしパラメータ** (`src/transcript/whisper_api.py`):
- モデル: `gpt-4o-transcribe`
- 言語: `ja`（日本語）
- Temperature: `0.1`
- レスポンスフォーマット: `srt`
- コンテキスト用カスタムプロンプトを含む
- レート制限回避のため、API呼び出し間に2秒のスリープ

### 翻訳API選定理由

プロジェクトでは3つの翻訳サービスを評価し、Google Translateを選定:
- **Google Translate** ✓ 採用: 繁体中国語（zh-TW）対応、50万字まで無料枠あり
- **DeepL** ✗ 高品質だが繁体中国語非対応
- **OpenAI GPT-3.5-turbo** ✗ レスポンスの行数が不安定、パース困難

## 実装の重要ポイント

### combine_srt.pyでのタイムスタンプ処理

チャンク結合時に字幕インデックスとタイムスタンプの両方を調整:
- チャンク位置に基づいて時間オフセットを追加（chunk_2は5:00開始、chunk_3は10:00開始など）
- チャンク境界を超えるタイムスタンプをクランプして重複を防止
- 全チャンクにわたって字幕インデックスを順次採番
- ミリ秒精度で正確な同期を実現

### モジュールインポートパターン

サブディレクトリのスクリプトは以下のパターンで`global_value.py`をインポート:
```python
from pathlib import Path
src_dir = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, str(src_dir))
import global_value as g
```

### ファイル処理順序

- 音声チャンクとSRTファイルは作成時刻またはファイル名でソートされ、順序を維持
- `input_movie/`ディレクトリ内で見つかった最初のMP4ファイルが自動的に処理対象として選択される

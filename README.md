# 🧊 Face Mosaic Tool

Python + OpenCV を使って、画像内の顔に自動でモザイク処理を施すツールです。  
複数の顔を検出し、サイズの大きいものから優先的に処理します。

---

## ✅ セットアップ手順

### 1. リポジトリをクローン

```bash
git clone https://github.com/frtkng/face-mosaic.git
cd face-mosaic
```

### 2. 仮想環境を作成して有効化
```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. 依存ライブラリのインストール
```bash
pip install -r requirements.txt
```

## 🧩 スクリプトの実行
画像ファイルと同じディレクトリで、以下を実行してください：
```bash
python face_mosaic.py
```
スクリプト中で指定された画像（例：PXL_20250501_080038842.jpg）に対してモザイクがかかり、mosaic_PXL_20250501_080038842.jpg として保存されます。

## 📦 ファイル構成
face_mosaic.py … 顔検出してモザイクをかけるメインスクリプト

requirements.txt … 使用ライブラリ一覧

.gitignore … .venv/など除外対象設定

## 📜 使用ライブラリ
OpenCV (cv2)

## 🛡️ 注意事項
モザイク処理は完全な匿名化ではありません。公開用途で使用する際は十分ご注意ください。

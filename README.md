# selenium-python-chrome-on-docker

## 事前準備 for Mac
VNCアクセスのための設定。
https://support.apple.com/ja-jp/guide/remote-desktop/apde0dd523e/mac

* システム環境設定 > 
* 共有 > 
* リモートマネージメントにチェック > 
* コンピュータ設定 > 
* VNC使用者が画面を操作することを許可にチェック > 
* パスワード入力 > 
* OK

## 使用方法
* app/src 内でクローラー記載
* $ sh build.sh > appコンテナ内に接続される
* vnc://localhost:15900に接続 
  * ブラウザのアドレスバー or Finder > 移動 > サーバへ接続
* パスワード: secret 入力
* $ python src/main.py > クローラー実行

## 
* docker-composeでappコンテナとchromeコンテナを起動
  * app: Selenium + Python実行環境
  * chrome: ブラウザ環境
* appコンテナでクローラーを実行し、chromeコンテナのブラウザにリモートアクセス。
* ローカルマシンからVNCアクセスしchromeコンテナ内のブラウザを表示

## 備考
* `.devcontainer/devcontainer.json`はVSCodeでの`ms-vscode-remote.remote-containers`用の設定
* ブラウザ表示が不要な場合はapp/src/utils/driver_option.pyの以下をコメントアウト

```py
...
options.add_argument('--headless')
...
```

## Forked from
ryoheiszk/python-selenium-on-docker

🙇

### 上記リポジトリからの変更内容
* ブラウザをFireFox -> Chrome
* Chrome Driver Option追加
* Macでの実行手順
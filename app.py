# Flaskという道具箱から、Flaskというクラス（設計図）をインポートする
from flask import Flask

# Flaskアプリの本体を作成
app = Flask(__name__)

# '/'（ルートURL、つまりWebサイトのトップページ）にアクセスがあった時の処理を定義
@app.route('/')
def hello():
    # ブラウザに「Hello, World from Flask!」という文字列を返す
    return 'Hello, World from Flask!'

# このスクリプトが直接実行された場合にのみ、以下の処理を行う
if __name__ == '__main__':
    # 開発用のWebサーバーを起動する
    # host='0.0.0.0' は、PCの外からもアクセスできるようにする設定
    # port=8080 は、8080番ポート（特定の通信窓口）を使う設定
    app.run(host='0.0.0.0', port=8080, debug=True)
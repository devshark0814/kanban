# Vueプロジェクトの作成
* コンテナに入って
<pre>vue init webpack XXXX</pre>

# Vueプロジェクトをローカルで動かすために
## config/index.js
* 16行目
  * host: '0.0.0.0',
* 21行目
  * poll: true

# Vueのレスポンスが遅い件
* node_modulesをwatchしてるからっぽい
## build/webpack.dev.conf.js
* 44行目に追加
  * ignored: /node_modules/,



# Fast-APIの起動
* コンテナに入って
<pre>uvicorn server:app --host 0.0.0.0 --port 3000 --reload</pre>

# Fast-APIのDod
<pre>http://localhost:3000/docs</pre>

# テーブルをスクリプトで作成
* コンテナにはいる
* <pre>python user.py</pre>
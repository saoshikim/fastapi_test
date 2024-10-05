1. 接続
&ssh slash@160.251.236.70

2. fastapiディレクトリに移動
&cd fastapi

3. 仮想環境の立ち上げ
&source venv/bin/activate

4. githubからクローンしたfastapi_testに移動
&cd fastapi_test

5. アプリを起動する
$uvicorn main:app --host 160.251.236.70 --port 8000

6. docs参照
http://160.251.236.70:8000/docs

※ 何故かアクセスできない。ポート8000を開いたと思うが、この辺に問題があるかも？


Ex1. 仮想環境から抜ける
deactivate

Ex2. SSH接続を解除する
logout

参考
https://zenn.dev/tau_dev/articles/e5e0a6d6df9724
https://libproc.com/fastapi-install-on-linux/#:~:text=%E7%9B%AE%E6%AC%A1.%20Python
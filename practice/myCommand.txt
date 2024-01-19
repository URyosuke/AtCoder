コンテスト用のディレクトリの作成(contestID はコンテストページの URL の末尾)
acc new contestID

テスト
oj t -c "python main.py"

提出
acc submit main.py -- -l 5055
acc s main.py -- --guess-python-interpreter pypy -w 0 -y

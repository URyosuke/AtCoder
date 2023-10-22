コンテスト用のディレクトリの作成(contestIDはコンテストページのURLの末尾)
acc new contestID

テスト
oj t -c " /Users/uesugiryousuke/anaconda3/bin/python main.py"

提出
acc submit main.py -- -l 5055
acc s main.py -- --guess-python-interpreter pypy -w 0 -y
# 12. 仮想環境とパッケージ =========================
'''
仮想環境を作るには、仮想環境を置くディレクトリを決めて、 
そのディレクトリのパスを指定して、 venv をスクリプトとして実行します
'''
python3 -m venv tutorial-env

'''
tutorial-env = ディレクトリ
一般的なディレクトリの場所 = .venv 
'''
# =========================
# 仮想環境を作ったら、それを有効化する必要があります。

# Windows の場合:
tutorial-env\Scripts\activate.bat

# Unix や Mac OS の場合:
source tutorial-env/bin/activate

'''
(このスクリプトは bash shell で書かれています。
csh や fish を利用している場合、代わりに利用できる 
activate.csh と activate.fish スクリプトがあります。)
'''

# =========================
'''
仮想環境を有効化すると、
シェルのプロンプトに利用中の仮想環境が表示されるようになり、
python を実行するとその仮想環境の Python を実行するようになります
'''
source ~/envs/tutorial-env/bin/activate
python3
# Python 3.5.1 (default, May  6 2016, 10:59:36)
#   ...
>>> import sys
>>> sys.path
# ['', '/usr/local/lib/python35.zip', ...,
# '~/envs/tutorial-env/lib/python3.5/site-packages']

# 12.3. pip を使ったパッケージ管理 =========================
'''
pip は "install" 、 "uninstall" 、 "freeze" など、
いくつかのサブコマンドを持っています。
'''
python3 -m pip install novas

# 特定のバージョンのパッケージをインストール
python3 -m pip install requests==2.6.0

# パッケージを最新版に更新
python3 -m pip install --upgrade requests

# コマンドに削除するパッケージ名を1つ以上指定
pip uninstall

# 指定されたパッケージの情報を表示
pip show requests

# 仮想環境にインストールされた全てのパッケージを表示
pip list

# =========================
'''
pip freeze はインストールされたパッケージ一覧を、
pip install が解釈するフォーマットで生成します。
一般的な慣習として、このリストを requirements.txt というファイルに保存します
'''
pip freeze > requirements.txt

cat requirements.txt
# novas==3.1.1.3
# numpy==1.9.2
# requests==2.7.0

# =========================
'''
requirements.txt をバージョン管理システムにコミットして、
アプリケーションの一部として配布することができます。
ユーザーは必要なパッケージを install -r でインストールできます
'''
python3 -m pip install -r requirements.txt


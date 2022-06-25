# 10.1. OSへのインターフェース =========================
'''
os モジュールは、オペレーティングシステムと対話するための多くの関数を提供しています
'''
import os

# Return the current working directory
os.getcwd()      
# 'C:\\Python310'

# Change current working directory
os.chdir('/server/accesslogs')   

# Run the command mkdir in the system shell
os.system('mkdir today')   

dir(os)
# <returns a list of all module functions>

help(os)
# <returns an extensive manual page created from the module's docstrings>

# =========================
'''
ファイルやディレクトリの日常的な管理作業のために、
より簡単に使える高水準のインターフェースが shutil モジュールで提供されています
'''
import shutil

shutil.copyfile('data.db', 'archive.db')
# 'archive.db'

shutil.move('/build/executables', 'installdir')
# 'installdir'

# 10.2. ファイルのワイルドカード表記 =========================
'''
glob モジュールでは、ディレクトリのワイルドカード検索から
ファイルのリストを生成するための関数を提供
'''
import glob

glob.glob('*.py')
# ['primes.py', 'random.py', 'quote.py']

# 10.3. コマンドライン引数  =========================
'''
コマンドライン引数は sys モジュールの argv 属性にリストとして保存されています。
'''
import sys

print(sys.argv)
# ['demo.py', 'one', 'two', 'three']

# =========================
'''
argparse モジュールは、コマンドライン引数を処理するための
更に洗練された仕組みを提供します
'''
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')

parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()

print(args)
# スクリプトは1つ以上のファイル名を抽出し、オプションで行数を表示します

# 10.4. エラー出力のリダイレクトとプログラムの終了 =========================
'''
sys モジュールには、 stdin, stdout, stderr を表す属性も存在します。 
stderr は、警告やエラーメッセージを出力
stdout がリダイレクトされた場合でも読めるようにする
'''
sys.stderr.write('Warning, log file not found starting a new one\n')
# Warning, log file not found starting a new one

sys.exit() 
# スクリプトを終了させるもっとも直接的な方法

# 10.5. 文字列のパターンマッチング =========================
'''
re モジュールでは、より高度な文字列処理のための正規表現を提供
'''

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# ['foot', 'fell', 'fastest']

re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# 'cat in the hat'

# 7.2. ファイルを読み書きする =========================

f = open('workfile', 'w', encoding="utf-8")

print(f)
# <_io.TextIOWrapper name='workfile' mode='w' encoding='utf-8'>

# =========================
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed # True

# with 文や f.close() の呼び出しによって閉じられた後に
# ファイルオブジェクトを使おうとするとそこで処理が失敗します
f.close()

f.read()
# ValueError: I/O operation on closed file.

# 7.2.1. ファイルオブジェクトのメソッド =========================

f.read() # 'This is the entire file.\n'

# ファイルの終端にすでに達していた場合、 
# f.read() は空の文字列 ('') を返します
f.read() # ''

# =========================
# f.readline() はファイルから 1 行だけを読み取ります。
# 改行文字 (\n) は読み出された文字列の終端に残ります。

f.readline()
# 'This is the first line of the file.\n'

f.readline()
# 'Second line of the file\n'

f.readline()
# ''

# =========================
# 複数行を読み取るには、ファイルオブジェクトに対してループを書く

for line in f:
    print(line, end='')

# This is the first line of the file.
# Second line of the file

# =========================
# f.write(string) は、string の内容をファイルに書き込み、
# 書き込まれた文字数を返します

f.write('This is a test\n') # 15

# =========================
# オブジェクトの他の型は、書き込む前に変換しなければなりません 
# -- 文字列 (テキストモード) と bytes オブジェクト (バイナリーモード) のいずれか

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s) # 18

# =========================
# ファイルオブジェクトの位置を変更するには、
# f.seek(offset, whence) を使います

f = open('workfile', 'rb+')

f.write(b'0123456789abcdef') # 16

# Go to the 6th byte in the file
f.seek(5) # 5

f.read(1) # b'5'

# Go to the 3rd byte before the end
f.seek(-3, 2) # 13

f.read(1) # b'd'


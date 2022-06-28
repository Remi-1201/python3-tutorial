# 10.7. インターネットへのアクセス =========================

# URL からデータを取得するための urllib.request
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline

# メールを送るための smtplib
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()

# 10.8. 日付と時刻 =========================
# dates are easily constructed and formatted
from datetime import date

now = date.today()
now
# datetime.date(2003, 12, 2)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
'''
%m = 12, %d = 02, %y = 03, %b = Dec, %Y = 2003, %A = Tuesday, %B = December
'''

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days # 14368

# 10.9. データ圧縮 =========================
'''
一般的なデータアーカイブと圧縮形式は、
以下のようなモジュールによって直接的にサポートされます: 
zlib, gzip, bz2, lzma, zipfile, tarfile。
'''
import zlib

s = b'witch which has which witches wrist watch'
len(s) # 41

t = zlib.compress(s)
len(t) # 37

zlib.decompress(t)
# b'witch which has which witches wrist watch'

zlib.crc32(s) # 226805979

# 10.10. パフォーマンスの計測 =========================
from timeit import Timer

Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.57535828626024577

Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.54962537085770791

# 10.11. 品質管理 =========================
'''
doctest モジュールでは、モジュールを検索してプログラムの
docstring に埋め込まれたテストの評価を行うためのツールを提供
'''
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest

doctest.testmod()   
# automatically validate the embedded tests

# =========================
'''
unittest モジュールは より網羅的なテストセットを
別のファイルで管理することができます
'''
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
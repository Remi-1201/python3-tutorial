# =========================
# 4.8.2. kwarg キーワード引数 

# 関数を kwarg = value という形式のキーワード引数 
# を使って呼び出すこともできます

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# この関数は以下のいずれかの方法で呼び出せます
# 1 positional argument
parrot(1000)                                          
# -- This parrot wouldn't voom if you put 1000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

# 1 keyword argument
parrot(voltage=1000)                                  
# The same result

# 2 keyword arguments
parrot(voltage=1000000, action='VOOOOOM')             
# -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

# 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             
# -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

# 3 positional arguments
parrot('a million', 'bereft of life', 'jump')         
# -- This parrot wouldn't jump if you put a million volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's bereft of life !

# 1 positional, 1 keyword
parrot('a thousand', state='pushing up the daisies')  
# -- This parrot wouldn't voom if you put a thousand volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's pushing up the daisies !

# 以下の呼び出しは不適切
parrot()                     
# required argument missing
parrot(voltage=5.0, 'dead')  
# non-keyword argument after a keyword argument
parrot(110, voltage=220)     
# duplicate value for the same argument
parrot(actor='John Cleese')  
# unknown keyword argument

# =========================
# いかなる引数も値を複数回は受け取れません

def function(a):
    pass

function(0, a=0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: function() got multiple values for argument 'a'

# =========================
#  **name はタプルを受け取る引数

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch


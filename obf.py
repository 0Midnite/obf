import base64
import zlib
import lzma
import marshal
from colorama import Fore, init
import os
from pathlib import Path
import random
import re
import string

def obf(code):
    def rmunnec(code):
        code = re.sub(r'#[^\n]*', '', code)
        code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
        return code

    def junkcmnts(code):
        obfuscated_lines = code.split("\n")
        new_lines = []
        for i in range(20):
            new_lines.append(f'{" " * random.randint(10, 50)}#{("0midnite.com" + (" " * random.randint(10, 50))) * random.randint(10, 50)}')
        for line in obfuscated_lines:
            new_lines.append(line)
            for i in range(20):
                new_lines.append(f'{" " * random.randint(10, 50)}#{("0midnite.com" + (" " * random.randint(10, 50))) * random.randint(10, 50)}')
        return "\n".join(new_lines)

    def randomvar():
        var = random.choice([
            '__' + ''.join(random.choices("O0", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("S5", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("Il", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("B8", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("Z2", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("PR", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("T7", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("PR", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("A4", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("Z7", k=random.randint(8, 64))),
            '__' + ''.join(random.choices("VY", k=random.randint(8, 64))),
        ])
        return var

    def junk():
        def randomdata():
            math = ['==', '+', '-', '*', '%', '^', '<<', '>>', '|', '^', '/', "<", ">"]
            data = random.choice([
                '"' + ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 64))) + '"',
                random.randint(99999, 9999999),
                '(' + "".join(f'{random.randint(99999, 9999999)},' for i in range(random.randint(1, 8))) + ')',
                '[' + "".join(f'{random.randint(99999, 9999999)},' for i in range(random.randint(1, 8))) + ']',
                '(' + "".join(f"'{''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 64)))}'," for i in range(random.randint(1, 8))) + ')',
                '[' + "".join(f"'{''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 64)))}'," for i in range(random.randint(1, 8))) + ']',
                f'{random.randint(99999, 9999999)}{random.choice(math)}{random.randint(99999, 9999999)}',
                '(' + "".join(f"{f'{random.randint(99999, 9999999)}{random.choice(math)}{random.randint(99999, 9999999)}'}," for i in range(random.randint(1, 8))) + ')',
                '[' + "".join(f"{f'{random.randint(99999, 9999999)}{random.choice(math)}{random.randint(99999, 9999999)}'}," for i in range(random.randint(1, 8))) + ']'
            ])
            return data

        junk = ';'.join(f"{randomvar()}={randomdata()}" for j in range(random.randint(16, 256)))
        return junk

    unnec = rmunnec(code)
    junkcmnted = junkcmnts(unnec)
    b16 = base64.b16encode(junkcmnted.encode("utf-8"))
    b32 = base64.b32encode(b16)
    b64 = base64.b64encode(b32)
    b85 = base64.b85encode(b64)
    zlibenc = zlib.compress(b85)
    lzmaenc = lzma.compress(zlibenc)
    marshalenc = marshal.dumps(lzmaenc)

    coderename = randomvar()
    execrename = randomvar()
    evalrename = randomvar()
    importrename = randomvar()
    compilerename = randomvar()
    final = f'''__obfuscator__="obfu.py"
__author__=("0Midnite", "https://0midnite.com")

{junk()};{execrename},{evalrename},{importrename},{compilerename}=eval(eval("chr(101)+chr(120)+chr(101)+chr(99)")),eval(eval("chr(101)+chr(118)+chr(97)+chr(108)")),eval(eval("chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)")),eval(eval("chr(99)+chr(111)+chr(109)+chr(112)+chr(105)+chr(108)+chr(101)"));{junk()};{coderename}={marshalenc};{junk()};{evalrename}("chr(48)+chr(77)+chr(105)+chr(100)+chr(110)+chr(105)+chr(116)+chr(101)+chr(35)+chr(55)+chr(52)+chr(54)+chr(50)");{junk()};{execrename}({compilerename}({importrename}({evalrename}("chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)")).b16decode({importrename}({evalrename}("chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)")).b32decode({importrename}({evalrename}("chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)")).b64decode({importrename}({evalrename}("chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)")).b85decode({importrename}({evalrename}("chr(122)+chr(108)+chr(105)+chr(98)")).decompress({importrename}({evalrename}("chr(108)+chr(122)+chr(109)+chr(97)")).decompress({importrename}({evalrename}("chr(109)+chr(97)+chr(114)+chr(115)+chr(104)+chr(97)+chr(108)")).loads({coderename}))))))),{evalrename}("chr(111)+chr(98)+chr(102)+chr(117)+chr(46)+chr(112)+chr(121)"),{evalrename}("chr(101)+chr(120)+chr(101)+chr(99)")));{junk()}'''

    return final
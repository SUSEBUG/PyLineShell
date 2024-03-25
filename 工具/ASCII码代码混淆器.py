#leeya_bug

code = input('请输入命令: ')
nums = input('请输入混淆次数(默认为1): ')
nums = int(nums) if nums != '' else 1

for iter in range(nums):
    res = f'chr({ord(code[0])})'
    code = code[1:]
    for i in code:
        res += f'+chr({ord(i)})'
    res = 'eval(eval(' + res + '))'
    code = res

print(code)
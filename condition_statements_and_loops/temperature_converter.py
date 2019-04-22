#!/usr/bin/env python3

temp = input('请输入摄氏或华氏温度数值（形如20c、35c、150f...）：')
type = temp[-1].upper()
value = int(temp[:-1])

if type == 'C':
  res = int(round(value/5*9 + 32))
elif type == 'F':
  res = int(round((value -32) / 9 * 5))
else:
  print('请输入有效温度格式')
  quit()

print('转换结果为：', res, ('华氏度' if type == 'C' else '摄氏度'))
quit()
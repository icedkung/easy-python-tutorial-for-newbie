import datetime
def fnumcount():
  nowsart = datetime.datetime.now()
  print ("เวลาเริ่มคือ : ")
  print (nowsart.strftime("%Y-%m-%d %H:%M:%S\n\n"))

  #ชื่อโปรแกรม
  print('โปรแกรมนับเลข')

  #รับค่า 3 ค่า
  fnum = int(input('1st num = '))
  rnum = int(input('range num = '))
  lnum = int(input('last num = '))

  print('\n')
  print('ผลลัพธ์')
  print(list(range(fnum,lnum,rnum)))

fnumcount()


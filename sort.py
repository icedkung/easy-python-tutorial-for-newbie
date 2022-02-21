
def sortnum():
 #define 
 number=[]

 #loop input
 print("โปรแกรมเรียงตัวเลข ระบุเลขที่ต้องการเรียง และระบุ 0 เพื่อเริ่มเรียง")
 while True:
     x=int(input("Num (0=หยุด) :"))
     if x<=0:
         break
     number.append(x)

#sorting tutorial

 #sorted output
 print("\nก่อนเรียง=>",number)
 number.sort()
 print("\nน้อยไปมาก=>",number)
 number.reverse()
 print("\nมากไปน้อย=>",number)
 print("เรียบร้อยแล้ว !")

#function call
sortnum()

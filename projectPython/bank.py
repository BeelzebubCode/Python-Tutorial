#โปรแกรมบัญชีธนาคาร

#data
account={"นายA":5000,"นายB":0}

def getBalance():
    print("ยอดเงินคงเหลือในบัญชี :",account)

def deposit(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ต้องป้อนตัวเลขเท่านั้น")
    if money < 0 :
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    print("ฝากเงินเข้าบัญชี A :",money)
    account["นายA"]+=money

def withDraw(money):
    if not type(money) is int:
        raise Exception("ต้องป้อนตัวเลขเท่านั้น")
    if money < 0 :
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money > account["นายA"] :
        raise Exception("ยอดเงินไม่พอถอน")
    print("ถอนเงินจากบัญชี A :",money)   
    account["นายA"]-=money

def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ต้องป้อนตัวเลขเท่านั้น")
    if money < 0 :
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money > account["นายA"] :
        raise Exception("ยอดเงินไม่พอโอน")
    print("ทำการโอนเงินไปที่บัญชี B :",money)
    account["นายB"]+=money
    account["นายA"]-=money


try:
    getBalance()
    print("----------------------------\n")

    #ฝากเงิน
    moneys=input("จำนวนเงินที่ฝากเข้าบัญชีนาย A :")
    if moneys.isnumeric():
        moneyI=int(moneys)
        deposit(moneyI)
    else :
        moneyF=float(moneys)
        deposit(moneyF)
    getBalance()
    print("\n----------------------------\n")

    #ถอนเงิน
    withdrawI=int(input("จำนวนเงินที่ต้องการถอนจากบัญชีนาย A :"))
    withDraw(withdrawI)
    getBalance()
    print("\n----------------------------\n")

    #โอนเงิน
    Transfer=input("จำนวนเงินที่ต้องการโอนให้ B จากบัญชี A :")
    if Transfer.isnumeric():
        transferI=int(Transfer)
        transfer(transferI)
    else :
        transferF=float(Transfer)
        transfer(transferF)
    getBalance()
    print("\n----------------------------\n")

except ValueError:
    print("กรุณาป้อนตัวเลขเท่านั้น")
except Exception as e :
     print(e)


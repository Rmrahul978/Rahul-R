print("Welcome to python hotel management system")
def getCustomerData():
    print("please fill following details")
    name=str(input("enter your name : "))
    age=int(input("enter your age: "))
    np=str(input("enter your native place: "))
    id=int(input("enter your govt id(any) number : "))
    mob_no=int(input("enter your mobile number: \n"))
    roomChoice()
def roomChoice():
    print("you entered  room selection page:\n")
    roomclass={
        "1.class A":"5000",
        "2.class B":"4000",
        "3.class C":"3000",
        "4.class D":"2000",
        "5.class E":"1000"
    }
    print("Availble room class and amount followed by:\n",roomclass)
    rc=int(input("enter the room class you want: "))
    if rc<=5:
        roomBooking(rc)    
    else:
        roomChoice()
def roomBooking(rc):
    print("you entered  room booking")
    if rc==1:
        print("you choosen class'A'")
        amountcalculate(rc)
    elif rc==2:
        print("you choosen class'B'")
        amountcalculate(rc)
    elif rc==3:
        print("you choosen class'C' ")
        amountcalculate(rc)
    elif rc==4:
        print("you choosen class'D'")
        amountcalculate(rc)
    elif rc==5:
        print("you choosen class'E'")
        amountcalculate(rc)
    else:
        roomChoice()
def amountcalculate(rc):
    d=int(input("enter how many days you want to stay: "))
    if rc==1:
        cash=d*5000
        print("you need to pay",cash)
        cashpay(cash)
    elif rc==2:
        cash=d*4000
        print("you need to pay",cash)
        cashpay(cash)
    elif rc==3:
        cash=d*3000
        print("you need to pay",cash)
        cashpay(cash)
    elif rc==4:
        cash=d*2000
        print("you need to pay",cash)
        cashpay(cash)
    elif rc==5:
        cash=d*1000
        print("you need to pay",cash)
        cashpay(cash)
    else:
        roomChoice()
def cashpay(cash):
    print("welcome to cash payment mode")
    print("************")
    print("do not press back button or close window while transection complete")
    upi=int(input("we have only UPI payment option press 1 to coninue: "))
    if upi==1:
        upi1=str(input("enter your UPI id: "))
        print("go to the merchant app and pay the bill")
        print("************")
        print("please wait your transcetion processing")
        print("************")
        print("transection completed your paid amount is",cash)
        greet()
    else:
        cashpay()
def greet():
    print("********successfully room booked******")
    print("******have a nice day ahed!********")
getCustomerData()


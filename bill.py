#light bill
# scenario 2

# name=input("enter your name")
# 
# 150-300 60rs per unit for commericial
# 150-300 40rs per unit for domestic
# 
# 300-450 85rs per unit for commericial
# 300-450 60rs per unit for domestic
# 
# 450-600 100rs per unit for commericial
# 450- 600 80rs per unit for domestic

name=input("enter your name:")
cust_t=int(input("which customer type are you?\npress 1. for commercial \n2. for domistic:\n "))

if cust_t==1: #commercial
    print(f"customer type : commercial \n invoice id : ")
    units=int(input("number of units you consumed?:"))
    if units>=450 and units <800:
        print(f" dear{name} as per your {units},  you will be charged as rp100/unit for commercial \n your bill of electricity for current month is \nRs {units*100}")
    elif units>=300 and units <450:
        print(f" dear{name} as per your {units},  you will be charged as rp85/unit for commercial \n your bill of electricity for current month is \nRs {units*85}")
        
    elif units>=150 and units<300:
        print(f" dear{name} as per your {units},  you will be charged as rp65/unit for commercial \n your bill of electricity for current month is \nRs {units*65}")

    else:
        print(f" dear{name} as per your {units},  you will be charged as rp150/unit for commercial \n your bill of electricity for current month is \nRs {units*150}")
     #surcharge=units+units/4
     #print(f"total bill with surcharge rs{units/4},now subtotal is {surcharge}")
      
elif cust_t==2: # domestic
    print(f"customer type : domestic \n invoice id : ")
    units=int(input("number of units you consumed?:"))
    if units>=450 and units <800:
        print(f" dear{name} as per your {units},  you will be charged as rp80/unit for  domestic \n your bill of electricity for current month is \nRs {units*80}")
    elif units>=300 and units <450:
        print(f" dear{name} as per your {units},  you will be charged as rp60/unit for  domestic \n your bill of electricity for current month is \nRs {units*60}")
        
    elif units<300:
        print(f" dear{name} as per your {units},  you will be charged as rp40/unit for  domestic \n your bill of electricity for current month is \nRs {units*40}")

    else:
        print(f" dear{name} as per your {units},  you will be charged as rp100/unit for  domestic \n your bill of electricity for current month is \nRs {units*100}")


import time
print("hello, wellcome to DV coffe shop")
time.sleep(3)
name = input("what is your name? \n")

if name == "hani" or name == "zana":
    bitch_status = input("are you evil?")
    good_things = int(input("how many good things you have done today?\n"))
    if bitch_status == "yes" and good_things < 4:
        print("get the fuck out of here")
        exit()
    else:
        time.sleep(3)
        print("\nwell hi " + name + " and welcome to DV coffe shop\n")  
else:
    print("\nwell hi " + name + " and welcome to DV coffe shop\n")

menu = "black coffe, espperso, latte, cappuccino"
time.sleep(2)
print( name + " what can i get you? here is the list of what we have\n" + menu)

order = input()

price = 7

if order == "latte":
    price = 13

quantity = input("how many can i get you?\n")

total = price * int(quantity)

print("sound good " + name + ",we have your " + quantity + " " + order + ", in just a seccond")

time.sleep(8)

print("\nalright " + name + " your total is, $" + str(total))
 






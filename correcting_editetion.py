import time
print("hello, wellcome to DV coffe shop")
name = input("what is your name? \n")

if name == "hani" or name == "zana":
    bitch_status = input("are you evil?")
    good_things = int(input("how many good things you have done today?\n"))
    if bitch_status == "yes" and good_things < 4:
        print("get the fuck out of here")
        exit()
    else:
        print("\nwell hi " + name + " and welcome to DV coffe shop\n")
else:
    print("\nwell hi " + name + " and welcome to DV coffe shop\n")

menu = "black coffe, espperso, latte, cappuccino"
print( name + " what can i get you? here is the list of what we have\n" + menu)

order = input()

price = 7

if order == "latte":
    price = 13
elif order == "black coffe":
    price = 20

if order == "latte":
  extra_ques = input("do you  wan't whipped cream?")

if extra_ques == "yes":
  sec_qes = input("that would be $18 \nwould  you like me to have that ready for you?")
else :
  extra_ques == "no"
  print("ok sir we will move on with the usal")


if extra_ques == "yes":
  price = 18
else :
  pass

if extra_ques and sec_qes == "no":
  price = 13
# if sec_qes == "no":
#   print("ok so the usal it is\n")
quantity = input("how many can i get you?")

total = price * int(quantity)

if extra_ques == "yes":
  print("sound good " + name + ",we have your " + quantity + " " + order + " with whipped cream" +", in just a seccond")
else:
  print("sound good " + name + ",we have your " + quantity + " " + order + ", in just a seccond")

#time.sleep(8)

print("\nalright " + name + " your total is, $" + str(total))


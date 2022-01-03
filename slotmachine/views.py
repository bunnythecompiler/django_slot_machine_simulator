from django.shortcuts import render,redirect 
#simulator packages 
from random import choice 
from random import random
import random

a = 1 
b = 5 
bank = 0 
refund = 0
def home(request): 
    global bank 
    global refund
    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        print(amount)
        
        win = ['won','lost']
        t = random.choice(win)
        random_odd = random.uniform(a,b)
        print('this is the random odd generated', random_odd)
        wit = amount * random_odd
        if t == "won":
            if wit > bank:
                print("the bank can't afford that , it has",round(bank,2))
                refund += amount
                refunds = f"we will refund you ${refund }"
                context = {
                    'refund':refunds
                }
                return render(request, 'slotmachine/home.html',context)
            else:
                print('you won')
                message = "you won "
                bank -= wit 
                all = f"Y0u have won, you have received { round(wit,2)} money left in the vault after winning is { round(bank,2)}"
                context = {
                    'won':all
                }
                return render(request, 'slotmachine/home.html',context)
        else:
            print("you have lost it all")
            bank += amount
            lost = f"you have lost, money in the  admin vault is {bank }, money you could have won  is {wit}"
            context = {
                'lost':lost
            }
            return render(request, 'slotmachine/home.html',context)
    return render(request, 'slotmachine/home.html')


def logs(request):
    refundables = f"You will be refunded ${refund } today."
    print(refundables)
    vault = f"Admin vault now has ${bank} left."
    context = {
        'refund':refundables,
        'bank':vault
    }
    return render(request, 'slotmachine/logs.html',context)



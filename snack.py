'''prepro onsite'''
def main():
    """snack"""
    money = int(input())
    water = int(input())
    snack_1 = int(input())
    snack_2 = int(input())
    snack_3 = int(input())
    money_left = money-water
    cost = 0
    cost1 = (money_left)%3
    ans1 = cost1 == 0 and snack_1*10 or cost1 == 1 and snack_1*15 or cost1 == 2 and snack_1*20
    cost += ans1
    money_left -= ans1
    cost2 = (money_left)%3
    ans2 = cost2 == 0 and snack_2*12 or cost2 == 1 and snack_2*15 or cost2 == 2 and snack_2*18
    cost += ans2
    money_left -= ans2
    cost3 = (money_left)%3
    ans3 = cost3 == 0 and snack_3*5 or cost3 == 1 and snack_3*7 or cost3 == 2 and snack_3*9
    cost += ans3
    money_left -= ans3
    if money < cost:
        print("Now you have %d left." %(money))
        print("You don't have enough money!")
    else:
        print("Now you have %d left." %(money_left))
        print("Here's your order!")
        print('Water: %d baht' %water)
        print('Snack number 1: %d baht' %(ans1))
        print('Snack number 2: %d baht' %(ans2))
        print('Snack number 3: %d baht' %(ans3))
main()

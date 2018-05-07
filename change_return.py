"""this program takes in number of cents and returns lowest number of change"""

print('How much change is there?')
change = int(input())

quarters = change // 25 

cents_remain = change - (25 * quarters)

dimes = cents_remain // 10

#dimes = cents_remain - (10 * dimes)

cents_remain = cents_remain - (10 * dimes)
                                           
nickels = cents_remain // 5

cents_remain = cents_remain - (5 * nickels)

#cents_remain = cents_remain - (10 * nickels)

pennies = cents_remain 



print("number of quarters", quarters)
print("number of dimes", dimes) 
print("number of nickels", nickels)
print("number of pennies", pennies)
print("number of cents_remain", cents_remain)


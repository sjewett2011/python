print('Galacticoconut')
print('which character type would you like to be?')
character = input() 
print('You can only have 100 magic and attack points combined, how many magic points do you want?')
magic = input()

points = int(magic)

attack_points = 100 - int(points)

print('Welcome to Galacticoconut, you are '+ character +' you have '+ str(int(points)) +' magic points and '+ str(int(attack_points)) +' attack points.')     

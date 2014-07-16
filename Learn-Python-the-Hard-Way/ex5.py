my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % ( my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, tru to get it exactly right
print "If I add %d, %d, and %d I get %d."% (
		my_age, my_height, my_weight, my_age + my_height + my_weight)

# round a floating point number

print "rounded pi is",round(3.14159265359)
print "How about rounding a integer?"
print "round(3) is",round(3)

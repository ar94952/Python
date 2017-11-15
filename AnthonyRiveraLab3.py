# Anthony Rivera
# CIS - 117 OL
# 09/08/2017
# Lab Assignment 3

total_cost = int(input('Please enter a total_cost:'))
if total_cost>=210:    

   print"14% discount coupon applied"
   total_cost *= 0.86


elif total_cost>150:

   print"12% discount coupon applied"
   total_cost *= 0.88


elif total_cost>=60:

   print"10% discount coupon applied"
   total_cost *= 0.90
   

elif total_cost>=10:

   print"8% discount coupon applied"
   total_cost *= 0.92   

else:
   print 'No coupon for purchases less than $10!'
print 'Now the total cost is ', total_cost

############################################################
# RESULT OF 5 DIFFERENT RUNS WITH DIFFERENT PRICES         #
# Please enter a total_cost:8% discount coupon applied     #
# Now the total cost is  9.2                               #
# Please enter a total_cost:10% discount coupon applied    #
# Now the total cost is  63.0                              #
# Please enter a total_cost:10% discount coupon applied    #
# Now the total cost is  135.0                             #
# Please enter a total_cost:12% discount coupon applied    #
# Now the total cost is  176.0                             #
# Please enter a total_cost:14% discount coupon applied    #
# Now the total cost is  197.8                             #
############################################################



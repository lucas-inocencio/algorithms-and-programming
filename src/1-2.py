# 1. How many seconds are there in 42 minutes 42 seconds?
print(42*60+42)
# 2562 seconds

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print(10/1.61)
# 6.21 miles

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
print(2562/(10/1.61)//60, 2562/(10/1.61)%60)
print((10/1.61)/(2562/60/60))
# 6 minutes and 52 seconds per mile. 8.73 miles per hour
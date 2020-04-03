#take users input
end_point = int(input('give me a number'))


#create a counter
count = 1

#print numbers starting at 1 ending at users input using while loop
#counts from 1 to the users end_point
while count <= end_point:
	
	#if users input is divisible by 3 AND 5 print fizz buzz
			if count % 3 == 0 and count % 5 == 0:
					print(‘fizzbuzz’)
				
			#elif users input is divisible by 3,
				elif count % 3 == 0:
					print(‘fizz’)
					

			#elif users input is divisible by 3, check if it’s divisible by 5
				elif count % 5 == 0:
					print (‘buzz’)

	#if not divisible by either, print the number
	print(count)

	#iterate count
	count += 1






#######another solution########
#take users input
end_point = int(input('give me a number'))

for i in range(1, end_point):
#if users input is divisible by 3 AND 5 print fizz buzz
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
        
    #elif users input is divisible by 3,
    elif i % 3 == 0:
        print('fizz')
            

    #elif users input is divisible by 3, check if it’s divisible by 5
    elif i % 5 == 0:
        print ('buzz')

    print(i)
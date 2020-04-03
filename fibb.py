#loop input amount of times, add current number to revious number, and print each current number
#fibonacci sequence ex 1, 1, 2, 3, 5, 8, 13, 21, 34....

#get users input
end_point = int(input('Give me a number '))


#create counts

count = 0
prev_prev_num = 1
previous_num = 0

#create loop that runs until users input is reached
while count <= end_point:
    current_num = previous_num + prev_prev_num
    print(current_num)


#reassign previous previous number to previous number
    prev_prev_num = previous_num
#reassign previous number to current number 
    previous_num = current_num


#add to counter
    count += 1
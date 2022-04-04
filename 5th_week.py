print('Enter array :')
num_list = list(map(int, input().split()))

print("Enter Command :")
cmd_list = list(map(int, input().split()))

print(num_list[cmd_list[0]-1:cmd_list[1]-1])
print(num_list[cmd_list[0]+cmd_list[2]-2])
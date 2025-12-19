startingLocation = 50
min = 0
max = 100
zero_count = 0
filePath = ("./sample_dir.txt")
with open(filePath, 'r') as file:
    for line in file:
        dir = line[0]
        num = int(line[1:])
        if dir == 'L':
            startingLocation -= num
            
            if startingLocation == 0:
                zero_count += 1
            else:
                while startingLocation < min:
                    zero_count+=1
                    print(f'The startinglocation is {startingLocation} the num is {num} at the start and the zero count is {zero_count}')
                    temp = abs(startingLocation)
                    startingLocation = max
                    startingLocation -= temp


                   
                    # print(f'the total zero count {zero_count}')
                    if startingLocation == 0:
                        zero_count +=1
                    print(f'The startinglocation is {startingLocation} the num is {num} at the end and the zero count is {zero_count}')
            # print(f'The Dial is rotated {line} to point at {startingLocation}')
        else:
            
            startingLocation += num
            while startingLocation >= max:
                zero_count+=1
                temp = startingLocation
                startingLocation = min
                temp -= max
                startingLocation += temp
                if(startingLocation == 0):
                    zero_count+=1
            # print(f'The Dial is rotated {line} to point at {startingLocation}')
print(f'The total times it landed on ZERO is : {zero_count}')



        # print(num)
        # print(dir)
        # print(line.strip())
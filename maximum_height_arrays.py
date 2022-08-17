'''
You are a scientist observing a peculiar planet ‘NINJA_LAND’. The surface of this planet is a flat X-Y plane. ‘N’ square-shaped meteorites are falling one by one into the planet on the X-axis from space.

With your years of experience and new technology, you have been able to accurately calculate the position of the leftmost X coordinate of meteors on ‘NINJA_LAND’ along with their size.

You store this information in a 2D matrix/list ‘METEORITES’ of size ‘N’ x 2 where ‘METEORITES[i][0]’ denotes the leftmost ‘X’ coordinate of meteor ‘i’ and ‘METEORITES[i][1]’ denotes its size.

As a meteorite ‘M’ falls on ‘NINJA_LAND’ at a specific location, and if some meteorite ‘N’ is already there at that location, then the current meteorite ‘M’ will stick on top of that previous meteorite ‘N’.

Your task is to find the current highest height of any meteorite after each meteorite falls from space. Formally, return an array/list ‘HEIGHTS’ where ‘HEIGHT[i]’ denotes the highest height so far after ‘i’ meteorites have fallen on ‘NINJA_LAND’.

Let ‘N’ = 3 and ‘METEORITES’ = [[1, 2], [2, 3], [6, 1]].
The position and size of each meteorite are: </br>
‘Meteorite1’:  At 1 position and size of 2.
‘Meteorite2’:  At 2 position and size of 3.
‘Meteorite3’:  At 6 position and size of 1.

So when the first meteorite falls maximum height till now is 2.
When the second meteorite falls maximum height till now is 5.
When the third meteorite falls maximum height till now is 5.

'''


def ninjaAndMeteorites(n, meteorites):
	# Write your code here.
	
    current_height = meteorites[0][1]
    min_x = meteorites[0][0]
    max_x = meteorites[0][0] + meteorites[0][1]


    print(f"current height till now is for 1st meteor {current_height}")

    for i in range(1,n):   
        if meteorites[i][0] < (meteorites[i-1][1] + meteorites[i-1][0]):
            current_height += meteorites[i][1]
        else:
            current_height = max(current_height,meteorites[i][1])

        print(f"current height till now for {i+1} metero is {current_height}")


ninjaAndMeteorites(5,[[4,6],[10,4],[9,1],[2,9],[5,10]]) 




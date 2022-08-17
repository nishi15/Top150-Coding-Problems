'''
‘N’ players are playing an online game and you are given the time in seconds each one requires to finish the game in the form of an array ‘A’. Now, the game requires to form pairs  of players such that the total time taken is divisible by 60 seconds.  More formally you need to find pairs with indices ( ‘i’ , ‘j’ ) such that ‘i’ < ‘j’ and ( A[i] + A[j] ) is divisible by 60.

N = 5
A = [ 30, 20, 30,40, 100 ]

Explanation : 

The valid pairs are : 

( 30, 30 ) as the sum is 60.
( 20, 40 ) as the sum is 60.
( 20, 100 ) as the sum is 120 which is divisible by 60.

Thus we output 3.
'''

def timingSum(a, n)-> int:
    freq = {}
    
    for i in a:
        rem = i%60
        if rem in freq:
            freq[rem] += 1
        else:
            freq[rem] = 1
    count = 0

    for i in freq:
        if i == 0:
            count += freq[0] // 2
            continue

        if i == 60//2:
            count += freq[60//2] // 2
            continue

        if i in freq and 60-i in freq:
            if freq[i] and freq[60-i]:
                count += 1
                freq[i] -= 1
                freq[60-i] -=1
                continue

    print(f'count is {count}')
    print(freq)

# timingSum([ 30, 20, 30,40, 100 ],5)

l = [30, 20, 30,40, 100]
c = 0

for i in range(len(l)):
    if (l[i]+l[i]) % 60 == 0:
        c +=1

print(c)
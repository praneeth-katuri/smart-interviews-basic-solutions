'''
A truck has two fuel tanks: a main tank and an additional tank. The fuel levels in both tanks are represented by two integers: mainTank, which represents the fuel in the main tank in litres, and additionalTank, which represents the fuel in the additional tank in litres.

The truck has a mileage of 10 kilometers per litre. Whenever 5 litres of fuel are consumed from the main tank, if the additional tank has at least 1 litre of fuel, 1 litre of fuel will be transferred from the additional tank to the main tank. Print the maximum distance that can be travelled with the given fuel.


Input Format

The first and only line of input contains two integers mainTank and additionalTank.


Output Format

Print the maximum distance that can be travelled with the given fuel.


Constraints

1 <= mainTank, additionalTank <= 100


Examples

Input 1

5 10


Output 1

60


Input 2

2 2


Output 2

20


Explanation

Example 1:

After spending 5 litre of fuel, fuel remaining is (5 - 5 + 1) = 1 litre and the distance travelled is 50km. After spending another 1 litre of fuel, no fuel gets injected in the main tank and the main tank becomes empty. Total distance travelled is 60km.

Example 2:

After spending 2 litre of fuel, the main tank becomes empty. Total distance travelled is 20km.
'''

def max_distance(mainTank, additionalTank):
    distance = 0
    fuel_consumed = 0

    while mainTank > 0:
        if mainTank >= 5:
            fuel_consumed += 5
            mainTank -= 5
            distance += 5 * 10
        else:
            fuel_consumed += mainTank
            distance += mainTank * 10
            mainTank = 0
        
        if fuel_consumed % 5 == 0 and additionalTank > 0:
            mainTank += 1
            additionalTank -= 1
    return distance

mainTank, additionalTank = map(int, input().split())
print(max_distance(mainTank, additionalTank))
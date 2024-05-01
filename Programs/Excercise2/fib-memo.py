# Name: Aidan Schaubhut
# Date: 4/7/2024
# Description: This program uses the idea of Memoization to increase the effeciency of
#              a function mimicing the fibonacci formula


from hashMap import HashMap

# create HashMap to store calculated values
hMap = HashMap()
def fib(n):
    # if already calculated for n, then retrieve result from HashMap and return it
    if n in hMap:
        return hMap[n]
    # if calculating for 0, then record result to HahsMap and return result
    if n == 0:
        hMap[0] = 0
        return hMap[0]
    # if calculating for 1, then record result to HahsMap and return result
    if n == 1:
        hMap[1] = 1
        return hMap[1]
    # if calculating for != 0, 1, value that is alredy in HashMap, then
    # calculate value according to Fib formula, record the result to HashMap
    # and return the result
    hMap[n] = fib(n - 1) + fib(n - 2)
    return hMap[n]

def main():
    print(fib(100))

main()

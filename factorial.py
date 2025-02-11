n = int(input("Für welche Zahl soll die Fakultät berechnet werden?\n"))
n = 5
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))

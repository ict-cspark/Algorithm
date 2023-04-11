N = int(input())

memory = [0] * 1000001

for n in range(2, N + 1):
    memory[n] = memory[n - 1] + 1

    if n%2 == 0:
        memory[n] = min(memory[n], memory[n//2] + 1)
    
    if n%3 == 0:
        memory[n] = min(memory[n], memory[n//3] + 1)

    
print(memory[N])
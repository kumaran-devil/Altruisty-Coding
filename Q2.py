s = input()
n_start = int(input())
start_indices = []
for _ in range(n_start):
    start_indices.append(int(input()))
n_end = int(input())
end_indices = []
for _ in range(n_end):
    end_indices.append(int(input()))

def count_frogs(s, start_indices, end_indices):
    results = []
    
    for start, end in zip(start_indices, end_indices):
        substring = s[start-1:end]
        
        first_stone = substring.find('|')
        last_stone = substring.rfind('|')
        
        if first_stone == -1 or last_stone == -1 or first_stone == last_stone:
            results.append(0)
        else:
            count = substring[first_stone + 1:last_stone].count('*')
            results.append(count)
    
    return results

output = count_frogs(s, start_indices, end_indices)
print(output)

N = int(input())
colors = []

def find_odd_colored_balloon(N, colors):
    color_count = {}
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    for color in colors:
        if color_count[color] % 2 != 0:
            return color
    
    return "All are even"

for _ in range(N):
    color = input().strip()
    colors.append(color)

print(f"[{find_odd_colored_balloon(N, colors)}]")

with open("17.txt", "r") as f:
    get_range = lambda r: (*map(int, r[2:].split("..")),)
    target_x_range, target_y_range = map(get_range, f.readline().strip()[13:].split(", "))

k = target_x_range[0]
min_x_vel = 0
while k > 0:
    min_x_vel += 1
    k -= min_x_vel

max_x_vel = target_x_range[1]

min_y_vel = target_y_range[0]
max_y_vel = -target_y_range[0]


highest_y = 0
count = 0
for x_vel in range(min_x_vel, max_x_vel+1):
    for y_vel in range(min_y_vel, max_y_vel+1):
        x, y = 0, 0
        vx, vy = x_vel, y_vel
        inner_highest_y = 0
        while True:
            x, y = x + vx, y + vy
            if y > inner_highest_y:
                inner_highest_y = y
            vx = max(0, vx - 1)
            vy -= 1
            if x > target_x_range[1] or y < target_y_range[0]:
                break
            if x >= target_x_range[0] and y <= target_y_range[1]:
                count += 1
                if inner_highest_y > highest_y:
                    highest_y = inner_highest_y
                break
            
print(highest_y)
print(count)
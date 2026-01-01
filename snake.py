clear()
change_hat(Hats.Dinosaur_Hat)
n = get_world_size()

for i in range(n):
	move(East)
while True:
	x = get_pos_x()
	y = get_pos_y()
	
	for _ in range(n-1):
		move(North)
	move(West)

	for _ in range(n-2):
		move(South)
	if x == 0:
		move(South)
		for _ in range(n):
			move(East)
	else:
		move(West)
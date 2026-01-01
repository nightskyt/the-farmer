clear()

do_a_flip()
n = get_world_size()

for i in range(n):
	for j in range(n):
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Cactus)
		use_item(Items.Fertilizer)
		move(East)
	move(North)


for raw in range(n):
	for i in range(n):
		is_swap = False
		for j in range(n):
			a = measure()
			b = measure(East)
			if j != n - 1 and a > b:
				swap(East)
				is_swap = True
			move(East)
		if not is_swap:
			break
	move(North)

for col in range(n):
	for i in range(n):
		is_swap = False
		for j in range(n):
			a = measure()
			b = measure(North)
			if j != n-1 and a > b:
				swap(North)
				is_swap = True
			move(North)
		if not is_swap:
			break
	move(East)
	
harvest()
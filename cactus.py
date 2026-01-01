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


for _ in range(n):
	for i in range(n):
		for j in range(n):
			a = measure()
			b = measure(East)
			if a > b:
				swap(East)
			move(East)
	move(North)

for _ in range(n):
	for i in range(n):
		for j in range(n):
			a = measure()
			b = measure(North)
			if a > b:
				swap(North)
			move(North)
	move(East)
	
harvest()
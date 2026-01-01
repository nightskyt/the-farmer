clear()
do_a_flip()
n = get_world_size()

while True:
	for i in range(n):
		for j in range(n):
			if can_harvest():
				harvest()
			if (i + j) % 2 == 0:
				plant(Entities.Tree)
			else:
				if get_ground_type() == Grounds.Soil:
					till()
				plant(Entities.Grass)

			if get_water() < 0.3:
				use_item(Items.Water)
			move(East)
		move(North)
		

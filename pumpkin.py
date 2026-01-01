def move_to(x, y):
	nx = get_pos_x()
	ny = get_pos_y()
	if x - nx > 0:
		for _ in range(x - nx):
			move(East)
	else:
		for _ in range(nx - x):
			move(West)	
	if y - ny > 0:
		for _ in range(y - ny):
			move(North)
	else:
		for _ in range(ny - y):
			move(South)	


n = get_world_size()
while True:
	clear()
	do_a_flip()
	for i in range(n):
		for j in range(n):
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Pumpkin)
			move(East)
		move(North)
	
	while True:
		dead_pumpkins = []
		
		for i in range(n):
			for j in range(n):
				if not can_harvest():
					x = get_pos_x()
					y = get_pos_y()
					dead_pumpkins.append((x, y))
				move(East)
			move(North)
		
		if len(dead_pumpkins) == 0:
			harvest()
			break
		
		while True:
			all_good = True
			for (x, y) in dead_pumpkins:
				move_to(x, y)
				plant(Entities.Pumpkin)
			
			# check again
			for (x, y) in dead_pumpkins:
				move_to(x, y)
				if not can_harvest():
					all_good = False
					plant(Entities.Pumpkin)
				else:
					dead_pumpkins.remove((x, y))
	
			if all_good:
				harvest()
				break
		break
		

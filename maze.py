n = 6
directions = [North, East, South, West]
dir_pos = {
	North: (0, 1),
	East: (1, 0), 
	South: (0, -1), 
	West:(-1, 0)
}
back_dir = {
	North: South,
	East: West, 
	South: North, 
	West: East
}

def next_dir_visited(direction):
	x, y = get_pos_x(), get_pos_y()
	nx, ny = dir_pos[direction]
	if (x+nx, y+ny) not in visited:
		return False
	return visited[(x+nx, y+ny)]
	

def gen_maze(n):
	plant(Entities.Bush)
	substance = n * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)


def dfs(direction, tx, ty, tpath=[]):
	x = get_pos_x()
	y = get_pos_y()
	if x == tx and y == ty:
		harvest()
		return True

	if get_ground_type() == Grounds.Grassland:
		till()
	visited[(x, y)] = True
	
	for dir in directions:
		if can_move(dir) and not next_dir_visited(dir):
			move(dir)
			tpath.append(dir)
			tpath_len = len(tpath)
			if dfs(dir, tx, ty, tpath):
				return True
			# back to old pos
			while len(tpath) >= tpath_len:
				trace_dir = tpath.pop()
				move(back_dir[trace_dir])
			visited[(x, y)] = False
	
	return False
			


while True:
	clear()
	path = list()
	visited = dict()
	gen_maze(n)
	tx, ty = measure()
	dfs(North, tx, ty)

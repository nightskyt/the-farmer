n = 10
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
	
	dirs = get_sorted_directions(tx, ty)
	for dir in dirs:
		if can_move(dir) and not next_dir_visited(dir):
			move(dir)
			tpath.append(dir)
			tpath_len = len(tpath)
			if dfs(dir, tx, ty, tpath):
				return True
			# back to old pos
			while len(tpath) >= tpath_len:
				trace_dir = tpath.pop()
				
				if get_ground_type() == Grounds.Soil:
					till()
				move(back_dir[trace_dir])
			# visited[(x, y)] = False
			
			nx, ny = dir_pos[dir]
			visited[(x+nx, y+ny)] = True
 			
	
	return False
			
def calculate_distance(x, y, tx, ty):
	return abs(x - tx) + abs(y - ty)

def get_sorted_directions(tx, ty):
	x, y = get_pos_x(), get_pos_y()
	valid_dirs = []
	for dir in directions:
		if can_move(dir) and not next_dir_visited(dir):
			dx, dy = dir_pos[dir]
			nx, ny = x + dx, y + dy
			dist = calculate_distance(nx, ny, tx, ty)
			valid_dirs.append((dist, dir))
	valid_dirs = bubble_sort_dirs(valid_dirs)
	sorted_dirs = []
	for item in valid_dirs:
		sorted_dirs.append(item[1])
	return sorted_dirs

def bubble_sort_dirs(dirs_with_dist):
	# 获取列表长度
	length = len(dirs_with_dist)
	
	# 外层循环：控制排序轮数（每轮确定一个最大元素的位置）
	for i in range(length):
		# 标记本轮是否有交换（优化：若无交换则已排好序，提前退出）
		swapped = False
		
		# 内层循环：比较相邻元素，将大的元素往后移
		# 每轮结束后，最后i个元素已排好序，无需再比较
		for j in range(0, length - i - 1):
			# 若前一个元素的距离 > 后一个，交换位置
			if dirs_with_dist[j][0] > dirs_with_dist[j+1][0]:
				# 手动交换两个元素
				temp = dirs_with_dist[j]
				dirs_with_dist[j] = dirs_with_dist[j+1]
				dirs_with_dist[j+1] = temp
				swapped = True
		
		# 若本轮无交换，说明列表已排序完成，提前退出
		if not swapped:
			break
	
	return dirs_with_dist
	

while True:
	clear()
	path = list()
	visited = dict()
	gen_maze(n)
	tx, ty = measure()
	tpath = []
	dfs(North, tx, ty, tpath)

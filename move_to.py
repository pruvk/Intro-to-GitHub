def move_to(target_x, target_y):
	current_x, current_y = get_pos_x(), get_pos_y()
	
	# Move X values
	while current_x != target_x:
		if current_x < target_x:
			move(East)
			current_x += 1
		else:
			move(West)
			current_x -= 1
			
	# Move y values
	while current_y != target_y:
		if current_y < target_y:
			move(North)
			current_y += 1
		else:
			move(South)
			current_y -= 1

move_to(0, 0)
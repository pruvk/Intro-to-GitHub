import move_to
import adjustWater

move_to.move_to(0, 0)

while True:
	
	for j in range(4):
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Grass)
			adjustWater.waterThreshold()
			
			move(North)
		move(East)
		
	for j in range(2):
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				
			current_x, current_y = get_pos_x(), get_pos_y()
			treeValueChecker = current_x + current_y
			
			if treeValueChecker % 2 == 0:
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Tree)
			else:
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Carrot)
			adjustWater.waterThreshold()
			
			move(North)
		move(East)

	for j in range(6):
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
			
			plant(Entities.Pumpkin)
			adjustWater.waterThreshold()
			move(North)
		move(East)
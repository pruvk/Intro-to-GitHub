def waterThreshold():
	if get_water() < 0.15:
		use_item(Items.Water)
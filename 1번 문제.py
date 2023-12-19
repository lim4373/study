# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def process_commands(n,m,commands):
	boxes = [0] * n
	
	for command in commands:
		box_number,operation, count = command
		box_index = box_number -1
		
		if operation == 1:
			boxes[box_index] +=count
		elif operation == 2:
			if boxes[box_index] >=count:
					boxes[box_index] -= count
					
					
	return boxes

n,m = map(int,input().split())
commands = [list(map(int,input().split())) for _ in range(m)]

result = process_commands(n,m,commands)
for count in result:
	print(count)
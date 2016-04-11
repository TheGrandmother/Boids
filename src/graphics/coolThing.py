import math as m

PI = 3.141592

if __name__ == "__main__":
	
	file = open("test.txt","w")
	
	t = 0
	s = 0.1
	lines = 3
	offs = (2*PI)/lines
	scale = 30
	stuff = 100;
	
	for bob in range(100):
		t = t + 0.15
		for index in range(lines):
			x = m.cos(t+offs*index)*scale + stuff
			y = m.sin((t+PI+offs*index))*scale + stuff
			dx = m.sin(t+s+offs*index)*5
			dy = m.cos((t+s+offs*index))*5
			file.write(str(index) + "," + str(x) + "," + str(y) + "," + str(dx) + "," + str(dy) + "\n")		



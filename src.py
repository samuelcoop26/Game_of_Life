import matplotlib.pyplot as plt
import sys
import numpy as np
import time
from matplotlib import animation

def main():
	global height
	global width	

	height=int(sys.argv[2])
	width=int(sys.argv[1])

	global data
	#data = np.random.randint(2,size=(height,width))
	data=np.random.choice([0, 1], size=(height,width), p=[.80, .2])	
	fig = plt.figure(figsize=(height,width))
	ax = fig.add_subplot(1,1,1)
	
	global im
	im = ax.imshow(data, animated=True,vmin=0,vmax=1,cmap='inferno')

	ani = animation.FuncAnimation(
		fig, 
		update_image, 
		interval=0)

	plt.axis('off')
	plt.show()

def update_image(i):
	global data
	newData=parse_pixels()
	data=newData
	im.set_array(data)
	
def parse_pixels():
	newData=np.zeros((height,width))
	for y in range(len(data)):
		for x in range(len(data[0])):
			count=check_neighbors(x,y)
			if data[y][x]==1:
				if count==2 or count==3:
					newData[y][x]=1
				else: newData[y][x]=0
			else: 
				if count==3:
					newData[y][x]=1
	return newData

def check_neighbors(x,y):
	count=0
	for j in range(-1,2,1):
		for k in range(-1,2,1):
			dx = x + k
			dy = y + j
			if dx>len(data[0])-1: 
				dx=0
			if dy>len(data)-1:
				dy=0	
			if dx == x and dy == y:
				count+=0
			elif data[dy][dx]==1: 
				count+=1
	return count						

def glider():
	#inital data conditions for a glider:
	global data
	data=np.zeros((height,width))
	data[int(height/2)][int(width/2)]=1
	data[int(height/2)-1][int(width/2)-1]=1
	data[int(height/2)+1][int(width/2)]=1
	data[int(height/2)+1][int(width/2)-1]=1
	data[int(height/2)][int(width/2)+1]=1



main()	

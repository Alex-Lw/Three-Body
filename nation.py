import random
import time
import math
import matplotlib.pyplot as plt
class nation(object):

	#init function
	def __init__(self):
		self.ip=0
		self.position=[]
		self.power=0
		self.defense=0
		self.nationkind=1
		self.alive=1
		self.kind=['weak','nice','noraml','evil']

	#set nation attribution
	def setNation(self,ip_t,position,power,defense,nationkind):
		self.ip=ip_t
		self.position.append(position)
		self.power=power
		self.defense=defense
		self.nationkind=nationkind
		self.alive=1

	def setPosition(self,p):
		self.position.append(p)

	def setIp(self,ip):
		self.ip = ip

	#action attack
	def attack(self,object_nation):
		if self.power>object_nation.defense:
			self.position.extend(object_nation.position)
			object_nation.alive=0
			if random.random()<0.1:
				self.power+=object_nation.power*random.random()
			else:
				if random.random()<0.1:
					self.power-=object_nation.power*random.random()
		else:
			if random.random()<0.05:
				self.position.extend(object_nation.position)
				object_nation.alive=0
			else:
				self.power-=object_nation.power*random.random()

	#activate decision function
	def activate(self):
		if random.random()<float(self.nationkind+1)/10:
			return True
		else:
			return False

	#show nation attribution
	def show(self):
		print self.ip, self.position, self.power ,self.defense ,self.kind[self.nationkind]



#find closest planet
def distance(na,nationlist):
	dis =1000*1000
	index =-1
	for i,n in enumerate(nationlist):
		if n.ip==na.ip:
			continue
		if n.alive==0:
			continue
		for p_list in n.position:
			for p_single in na.position:
				dis_tmp = abs(p_list[0]-p_single[0])**2+abs(p_list[1]-p_single[1])**2
				if dis_tmp>0 and dis_tmp < dis:
					dis=dis_tmp
					index= i
	return index

#show current state of galaxy
def showstate(nationlist):
	color=['b','c','r','g','k','m','w','y']
	for na in nationlist:
		x=[]
		y=[]
		if na.alive==1:
			for po in na.position:
				x.append(po[0])
				y.append(po[1])
		plt.plot(x,y,'o'+color[na.ip%8])
	plt.show()
	plt.clf()

#show final result distribution
def showdistribute(list):
	sum_list=sum(list)
	list_tmp=[]
	for data in list:
		list_tmp.append(float(data)/sum_list)
	print list_tmp
	plt.bar([0,1,2,3], list_tmp, 0.35, color='b')
	#plt.show()

	return list_tmp

def makeNewNationlist():
	nationlist=[]
	for i in range(100):
		nation_tmp=nation()
		nation_tmp.setIp(i+1)
		nation_tmp.setPosition([int(1000*random.random()),int(1000*random.random())])
		nationlist.append(nation_tmp)
	return nationlist
#run game once
def run():
	nationlist=makeNewNationlist()
	showstate(nationlist)
	
	for i in range(10):
		temp=[]
		if len(nationlist)>=2:
			for nation in nationlist:
				if random.random()<0.5:
					temp.append(nation)
		nationlist=temp
		showstate(nationlist)
	
	return
	'''
	#initialization
	nationlist=[]
	for i in range(100):
		nation_tmp=nation()
		p=[int(1000*random.random()),int(1000*random.random())]
		nation_tmp.setNation(i,p,100*random.random(),100*random.random(),int(1000*random.random())%4)
		nationlist.append(nation_tmp)
		#nation_tmp.show()
		#time.sleep(0.5)


	#run game
	count=0
	for i in range(1000):
		for na in nationlist:
			if na.alive==1 and na.activate():
				b=distance(na,nationlist)
				if b==-1:
					break
				na.attack(nationlist[b])
		sum_alive=0
		count+=1
		for na in nationlist:
			if na.alive==1:
				sum_alive+=1
		print 'step: '+str(count)+" "+str(sum_alive)
		if sum_alive==1:
			showstate(nationlist)
			break

		#if i%10==0:
		showstate(nationlist)

	for na in nationlist:
				if na.alive==1:
					#na.show()
					return na.nationkind
	'''

#main function
if __name__ == "__main__":
	run()


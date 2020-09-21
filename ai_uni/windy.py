import numpy as np
import os
import time
import matplotlib.pyplot as plt
import random as rn

class windy:
	def __init__(self):
		self.width = 8
		self.height = 7
		self.map = np.array(['0']*56).reshape([self.height,self.width])
		self.wind1 = [3,4,5,8]
		self.wind2 = [6,7]
		self.actionspace = 4
		self.observation = 56
		self.action = {0:'left',1:'up',2:'right',3:'down'}
		self.goal = [3,7]

	def reset(self):
		self.state = [3,0]
		self.map = np.array(['0']*56).reshape([self.height,self.width])
		self.map[self.state[0],self.state[1]] = 'X'
		return self.state

	def step(self,action):
		if action == 0:
			if self.state[1] != 0:
				self.state[1] -= 1
		elif action == 1:
			if self.state[0] != 0:
				self.state[0] -= 1
		elif action == 2:
			if self.state[1] != self.width - 1:
				self.state[1] += 1
		elif action == 3:
			if self.state[0] != self.height -1:
				self.state[0] +=1
		else:
			print('wrong input')
		
		#windy
		if self.state[1] in self.wind1 + self.wind2:
			if self.state[1] in self.wind1:
				if self.state[0] != 0:
					self.state[0] -= 1
				else:
					if self.state[0] >= 2:
						self.state[0] -= 2
					elif self.state[0] == 1:
						self.state[0] -= 1

		self.map = np.array(['0']*56).reshape([self.height,self.width])
		self.map[self.state[0],self.state[1]] = 'X'

		if self.state == self.goal:
			return self.state,0,True,None
		else:
			return self.state,-1,False,None


def rargmax(vector):
	m = np.amax(vector)
	ind = np.nonzero(vector == m)[0]
	return rn.choice(ind)

def arrtoind(array,width):
	ind = array[0]*width+array[1]
	return ind


def Sarsa(max_step,rendor):
	env = windy()

	Q = np.zeros([env.observation,env.actionspace])

	global_step = 0

	alpha = 0.5
	epsilon = 0.1

	episode = 0
	plot_graph = []

	while global_step <= max_step:
		episode += 1
		state = env.reset()

		done = False
		step = 0
		total_reward = 0
		while not done:
			if rendor:
				env.render()
			step += 1
			global_step += 1
			plot_graph.append(episode)
			
			if epsilon > np.random.rand(1):
				action = np.random.randint(env.actionspace)
			else:
				action = rargmax(Q[arrtoind(state, env.width), :])

			next_state,reward,done,_ = env.step(action)
			total_reward += reward
			
			Q[arrtoind(state, env.width), action] += (
                    alpha * (reward + (Q[arrtoind(next_state, env.width), action])
                             - Q[arrtoind(state, env.width), action]))

			state = next_state[:]

		print('Sarsa | Episode : {:5.0f} Step : {:5.0f} reward : {:5.0f}'.format(episode,step,total_reward))
	
	#np.save('QValue/Sarsa_value',Q)
	#np.savetxt('QValue/Sarsa_value.txt',Q)

	direction = np.array(['L','U','R','D'])

	Q = np.argmax(Q,axis=1)
	optimal_policy = np.chararray([env.observation],unicode=True)

	for i in range(env.actionspace):
		optimal_policy[Q==i] = direction[i]

	optimal_policy = optimal_policy.reshape([env.height,env.width])

	#np.savetxt('OptimalPolicy/optimal_Sarsa.txt',optimal_policy,delimeter='',fmt='%s')

	return plot_graph

def Qlearn(max_step,render):
	env = windy()

	Q = np.zeros([env.observation,env.actionspace])

	global_step = 0

	alpha = 0.5
	epsilon = 0.1

	episode = 0
	plot_graph = []

	while global_step <= max_step:
		episode += 1
		state = env.reset()

		done = False
		step = 0
		total_reward = 0
		while not done:
			if render:
				env.render()
			step += 1
			global_step += 1
			plot_graph.append(episode)

			if epsilon > np.random.rand(1):
				action = np.random.randint(env.actionspace)
			else:
				action = rargmax(Q[arrtoind(state,env.width), :])

			next_state,reward,done,_ = env.step(action)
			total_reward += reward
			
			Q[arrtoind(state,env.width),action] += (alpha*(reward + np.max(Q[arrtoind(next_state,env.width),:]) - Q[arrtoind(state,env.width),action]))

			state = next_state[:]

		print('Qlearn | Episode : {:5.0f} Step : {:5.0f} reward : {:5.0f}'.format(episode,step,total_reward))

	#np.save('QValue/QLearning_value',Q)
	#np.savetxt('QValue/QLearning_value.txt',Q)

	direction = np.array(['L','U','R','D'])

	Q = np.argmax(Q,axis=1)
	optimal_policy = np.chararray([env.observation],unicode=True)

	for i in range(env.actionspace):
		optimal_policy[Q==i] = direction[i]

	optimal_policy = optimal_policy.reshape([env.height,env.width])

	#np.savetxt('OptimalPolicy/optimal_Qlearning.txt',optimal_policy,delimeter='',fmt='%s')

	return plot_graph

def main():
	max_iter = 20000
	render = False
	sarsalearning = Sarsa(max_iter,render)

	qlearning = Qlearn(max_iter,render)

	plt.xlim([0,max_iter*1.1])
	plt.plot(qlearning,'b',label = 'QL')
	plt.plot(sarsalearning,'g',label='SARSA')
	plt.legend(bbox_to_anchor=(0.,1.02,1.,.102),loc=3,ncol=2,mode="expand",borderaxespad=0.)
	plt.show()

if __name__ == '__main__':
	main()
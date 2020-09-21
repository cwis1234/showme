import numpy as np
from sklearn import datasets

def relu(z):
	return np.maximum(0,z)

def sffunc(data):
	predcition = data - (data.max(axis=1).reshape([-1,1]))
	sf = np.exp(predcition)
	sf = sf / sf.sum(axis=1).reshape([-1,1])
	return sf

def loss(z,y,w):
	size = y.shape[0]
	cost = -np.log(z[np.arange(len(z)),np.argmax(y,axis=1)]).sum()
	cost /= size
	return cost

def relu_grad(x):
	x[x>=0]=1
	x[x<0]=0
	grad = x
	return grad

class MLP:
	def __init__(self,rate = 0.01,threshhold = 0.001,max_iteration = 100,number_hidden_layer = 2):
		self.rate = rate
		self.epoch = max_iteration
		self.threshhold = threshhold
		self.hiddendep = number_hidden_layer
		self.weight = {}
		return

	def setlayer(self,layer_number,input_size,output_size):
		self.weight['W'+str(layer_number)] = np.random.randn(input_size,output_size)
		self.weight['b'+str(layer_number)] = np.zeros(output_size)
		return

	def gradient(self,pred,x,y):
		size = y.shape[0]
		dy = (pred - y) / size
		a = np.dot(x,self.weight['W0']+self.weight['b0'])
		z = relu(a)
		grad = {}

		for j in range(0,self.hiddendep+1):
			Wkey = 'W'+str(j)
			bkey = 'b'+str(j)
			Wnextkey = 'W'+str(j+1)
			Wbefkey = 'W'+str(j-1)

			if j == self.hiddendep:
				t = np.dot(x,self.weight['W0'])+self.weight['b0']
				t = relu(t)
				gradient = np.dot(t.T,dy)
				grad[Wkey] = gradient
				grad[bkey] = np.sum(dy,axis=0)

			elif j == 0:
				da = np.dot(dy,self.weight[Wnextkey].T)
				dz = relu_grad(a)*da
				grad[Wkey] = np.dot(x.T,dz)
				grad[bkey] = np.sum(dz,axis=0)

			else:
				pass
		return grad

	def learning(self,x,y):
		input_size = x.shape[1]

		self.weight['W0'] = np.random.randn(input_size,len(self.weight['W1']))
		self.weight['b0'] = np.zeros(len(self.weight['W1']))

		for i in range(self.epoch):
			z = np.dot(x,self.weight['W0']) + self.weight['b0']
			z = relu(z)

			for j in range(1,self.hiddendep+1):

				if j == self.hiddendep:
					z = np.dot(z,self.weight['W'+str(j)]) + self.weight['b'+str(j)]
					z = sffunc(z)

				else:
					z=np.dot(z,self.weight['W'+str(j)])+self.weight['b'+str(j)]
					z = relu(z)
			
			cost = loss(z,y,self.weight['W'+str(self.hiddendep)])

			grad = self.gradient(z,x,y)

			for j in range(1,self.hiddendep + 1):
				W_key = 'W'+str(j)
				b_key = 'b'+str(j)
				self.weight[W_key] -= self.rate*grad[W_key]
				self.weight[b_key] -= self.rate*grad[b_key]
			if cost< self.threshhold:
				return
			
			print ("Iter(Epoch): %s, Loss: %s" % (i, cost))

		return

	def predict(self,x):
		a = np.dot(x,self.weight['W0']) + self.weight['b0']
		z = relu(a)

		for j in range(1,self.hiddendep + 1):
			W_key = 'W'+str(j)
			b_key = 'b'+str(j)
			W = self.weight[W_key]
			b = self.weight[b_key]

			if j == self.hiddendep:
				a = np.dot(z,W)+b
				y = sffunc(a)
				y = np.argmax(y,1)
				return y
			else:
				a = np.dot(z,W)+b
				z = relu(a)
		return False

def main():
	print('input minibatch size')
	#minibatch = int(input())
	print('input epoch size')
	#num_iteration = int(input())
	minibatch = 50
	epoch = 100

	skdataset = datasets.fetch_mldata('MNIST original',data_home = './')
	size = len(skdataset.target)
	dim = len(skdataset.data[0])
	w = np.random.uniform(-10,10,size=dim)
	b = np.random.uniform(-10,10)
	train_size = int(0.85*size)
	dev_size = int(0.05*size)
	test_size = int(0.1*size)
	sk_train_input = skdataset.data[0:train_size]
	sk_dev_input = skdataset.data[train_size:dev_size+train_size]
	sk_test_input = skdataset.data[dev_size+train_size:dev_size+train_size+test_size]
	sk_train_target = skdataset.target[0:train_size]
	sk_dev_target = skdataset.target[train_size:train_size+dev_size]
	sk_test_target = skdataset.target[train_size+dev_size:train_size+dev_size+test_size]

	train_size = sk_train_input[0]
	target = np.array(sk_train_target,np.int32)
	a = np.unique(target,axis=0)
	b = a.shape[0]
	y = np.eye(b)[target].astype(int)

	sk_train_input = sk_train_input / 255

	mlp = MLP(rate=0.01,threshhold=0.001,max_iteration=epoch,number_hidden_layer=1)
	mlp.setlayer(1,64,10)
	mlp.learning(sk_train_input,y)







	return

if __name__=="__main__":
	main()
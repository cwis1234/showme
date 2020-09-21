import numpy as np
from sklearn import datasets


def softmax(data):
	prediction = data - (data.max(axis=1).reshape([-1,1]))
	sf = np.exp(prediction)
	sf /= sf.sum(axis=1).reshape([-1,1])
	return sf

def loss(sf,y):
	size = y.shape[0]

	cost = -np.log(sf[np.arange(len(sf)),np.argmax(y,axis=1)]).sum()
	cost /= size
	return cost

def gradient(pred,x,y):
	size = y.shape[0]
	dy = (pred - y) / size
	grad = np.dot(x.T,dy)
	return grad

def softmaxregression(hyperparameter,data,target,dev_input,dev_target,test_input,test_target):
	max_iteration = hyperparameter['num_iteration']
	rate = hyperparameter['rate']
	threshhold = hyperparameter['threshhold']
	batch_size = hyperparameter['batch_size']
	num_case = data.shape[0]
	num_feature = data.shape[1]
	#one-hot encording
	num_class = target.shape[1]
	print(num_case)
	print(num_feature)
	print(num_class)

	w = np.random.randn(num_feature,num_class) / np.sqrt(num_feature / 2)
	rnd_idx = np.arange(data.shape[0])
	num_step = int(np.ceil(num_case/batch_size))
	for i in range(max_iteration):

		np.random.shuffle(rnd_idx)
		data = data[rnd_idx]
		target = target[rnd_idx]

		for step in range(num_step):
			start = step*batch_size
			end = min(num_case,(step+1)*batch_size)
			x = data[start:end]
			y = target[start:end]

			predict = np.dot(x,w)
			sf = softmax(predict)
			L = loss(sf,y)
			grad = gradient(sf,x,y)
			w -= rate*grad


		
		devp = np.dot(dev_input,w)
		devsf = softmax(devp)
		devL = loss(devsf,dev_target)

		testp = np.dot(test_input,w)
		testsf = softmax(testp)
		testL = loss(testsf,test_target)

		print(('Epoch {:3d} '
               'train Loss {:.5f} '
               'dev Loss {:.5f}'
			   'test Loss {:.5f}\n').format(i,L,devL,testL))


	pred = np.dot(test_input,w)
	sff = softmax(pred)


	return

def main():

	hyperparameter = {
		'rate' :0.1,
		'threshhold': 0.01,
		'num_iteration': 1000,
		'batch_size': 50
		}
	mnist = datasets.fetch_mldata('MNIST original',data_home = './')
	x=np.array(mnist.data)
	x = x / 123
	target=np.array(mnist.target,np.int32)
	
	a = np.unique(target,axis=0)
	b = a.shape[0]
	y = np.eye(b)[target].astype(int)

	rnd_idx = np.arange(x.shape[0])

	np.random.shuffle(rnd_idx)
	x = x[rnd_idx]
	y = y[rnd_idx]
	train_input = x[0:1000]
	train_target = y[0:1000]
	dev_input = x[1000:1050]
	dev_target = y[1000:1050]
	test_input = x[1050:1200]
	test_target = y[1050:1200]
	

	softmaxregression(hyperparameter,train_input,train_target,dev_input,dev_target,test_input,test_target)

	return

if __name__ == "__main__":
	main()
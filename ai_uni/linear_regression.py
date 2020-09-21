import numpy as np
import gen_random_dataset as gen
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error, r2_score


def randomlinear(size_batch,num_iteration,alpha):

	tw,tb,train_input,train_target,dev_input,dev_target,test_input,test_target = gen.generate(10,10,1000)
	#size = len(1000)
	dim = 10
	w = np.random.uniform(-1000,1000,size=dim)
	b = np.random.uniform(-1,1)

	
	epoch = num_iteration
	minibatch = size_batch
	num_train_cases = train_input.shape[0]
	num_dev_cases = dev_input.shape[0]
	num_test_cases = test_input.shape[0]
	
	rnd_idx = np.arange(train_input.shape[0])
	num_step = int(np.ceil(num_train_cases/minibatch))
	rate = alpha

	for ep in range(epoch):
		np.random.shuffle(rnd_idx)
		train_input = train_input[rnd_idx]
		train_target = train_target[rnd_idx]
		for step in range(num_step):
			start = step * minibatch
			end = min(num_train_cases,(step+1)*minibatch)
			x = train_input[start:end]
			y = train_target[start:end]
		
			predict = np.dot(x,w) + b

			loss = np.sum((predict-y)**2) / (2*minibatch)
			dldw = np.dot(x.T,predict-y) / minibatch
			dldb = np.sum((predict - y) / minibatch)
			w = w - rate*dldw
			b = b - dldb


			

		TPD = np.dot(train_input,w)+b
		TE = np.sum((TPD - train_target)**2) / (2*num_train_cases)
		DPD = np.dot(dev_input,w)+b
		DE = np.sum((DPD - dev_target)**2) / (2*num_dev_cases)
		TEPD = np.dot(test_input,w) + b
		TEE = np.sum((TEPD - test_target)**2) / (2*num_test_cases)
		TWWE = np.sum((tw - w)**2)/dim

		print(('Epoch : {:3d} ' 'Train Error : {:.5f} ' 'Dev Error : {:.5f} '
		  'Test Error : {:.5f} ' 'tw,w Error : {:.5f}').format(ep,TE,DE,TEE,TWWE))

		if TWWE < 0.001:
			print('learning complete')
			break


	return


def sklinear(size_batch,num_iteration,alpha):


	skdataset = datasets.load_diabetes()
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
	
	epoch = num_iteration
	minibatch = size_batch
	num_train_cases = sk_train_input.shape[0]
	num_dev_cases = sk_dev_input.shape[0]
	num_test_cases = sk_test_input.shape[0]
	rnd_idx = np.arange(sk_train_input.shape[0])
	num_step = int(np.ceil(num_train_cases/minibatch))
	rate = alpha
	for ep in range(epoch):
		np.random.shuffle(rnd_idx)
		sk_train_input = sk_train_input[rnd_idx]
		sk_train_target = sk_train_target[rnd_idx]

		TPD2 = np.dot(sk_train_input,w)+b
		TE2 = np.sum((TPD2 - sk_train_target)**2) / (2*num_train_cases)

		for step in range(num_step):
			start = step * minibatch
			end = min(num_train_cases,(step+1)*minibatch)
			x = sk_train_input[start:end]
			y = sk_train_target[start:end]
		
			predict = np.dot(x,w) + b

			loss = np.sum((predict-y)**2) / (2*minibatch)
			dldw = np.dot(x.T,predict-y) / minibatch
			dldb = np.sum((predict - y) / minibatch)
			w = w - rate*dldw
			b = b - dldb


			

		TPD = np.dot(sk_train_input,w)+b
		TE = np.sum((TPD - sk_train_target)**2) / (2*num_train_cases)
		DPD = np.dot(sk_dev_input,w)+b
		DE = np.sum((DPD - sk_dev_target)**2) / (2*num_dev_cases)
		TEPD = np.dot(sk_test_input,w) + b
		TEE = np.sum((TEPD - sk_test_target)**2) / (2*num_test_cases)

		
		print(('Epoch : {:3d} ' 'Train Error : {:.5f} ' 'Dev Error : {:.5f} '
		  'Test Error : {:.5f} ').format(ep,TE,DE,TEE))

		if abs(TE - TE2) < 0.001: # early stopping
			print('learning complete')
			break
	return

def main():

	#print('input N. N is number of data')
	#N = int(input())
	#print('input minibatch.')
	#minibatch_size = int(input())
	#train_input,train_target,dev_input,dev_target,test_input,test_target = gen.generate(10,10,N)
	print('input epoch')
	num_iter = int(input())
	print('input batch size')
	batch = int(input())
	print('select sk data learning or random data learning. sk is 1 random is 2')
	ab = int(input())
	if a== 1:
		sklinear(batch,num_iter,0.01)
	elif a == 2:
		randomlinear(batch,num_iter,0.01)
	else:
		print('wrong input.')








if __name__ == '__main__':
	main()
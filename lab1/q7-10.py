import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

tensor1 = torch.rand(2, 3).to(device)
tensor2 = torch.rand(2, 3).to(device)

print("Tensor1 on GPU:", tensor1)
print("Tensor2 on GPU:", tensor2)

tensor1 = tensor1.T 

result_gpu = torch.matmul(tensor1, tensor2)  # Shape (3, 3)
print("Matrix Multiplication on GPU:", result_gpu)
max_value = result_gpu.max()
min_value = result_gpu.min()

print("Max Value:", max_value)
print("Min Value:", min_value)

max_index = result_gpu.argmax()
min_index = result_gpu.argmin()

print("Max Index:", max_index)
print("Min Index:", min_index)

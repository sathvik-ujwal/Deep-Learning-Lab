import torch

tensor1 = torch.randint(0, 10, (7,7))
tensor2 = torch.randint(0, 10, (1, 7))

tensor2_transposed = tensor2.transpose(0, 1)
result = torch.matmul(tensor1, tensor2_transposed)
print(result)
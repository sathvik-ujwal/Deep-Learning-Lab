import torch
import numpy as np

np_array = np.array([1, 2, 3, 4, 5])
tensor = torch.from_numpy(np_array)
print(np_array)
print(tensor)

tensor_to_numpy = tensor.numpy()
print(tensor_to_numpy)
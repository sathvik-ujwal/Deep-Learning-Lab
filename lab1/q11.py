import torch

torch.manual_seed(7)
tensor3 = torch.rand(1, 1, 1, 10)
reshaped_tensor = tensor3.squeeze()

print("Original Tensor Shape:", tensor3.shape)
print("Reshaped Tensor Shape:", reshaped_tensor.shape)
print("Original Tensor:", tensor3)
print("Reshaped Tensor:", reshaped_tensor)

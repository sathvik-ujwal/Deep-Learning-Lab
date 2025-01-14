import torch

tensor = torch.arange(9)
print(tensor)

#reshape
reshaped_tensor = torch.reshape(tensor, (3, 3))
print(reshaped_tensor)

# viewing
view_tensor = tensor.view(3,3)
print(view_tensor)

#stacking
tensor1 = torch.tensor([1, 3])
tensor2 = torch.tensor([3, 4])
stacked_tensor = torch.stack([tensor1, tensor2], dim=0)
print(stacked_tensor)

new_tensor = torch.zeros(1, 2, 3)
print(new_tensor)
squeeze_tensor = torch.squeeze(new_tensor, dim=0)
print(squeeze_tensor)
unsqueeeze_tensor = torch.unsqueeze(squeeze_tensor, dim=0)
print(unsqueeeze_tensor)



import torch

#Returns a view of the original tensor input with its dimensions permuted.
tensor = torch.randn(2, 3, 5)
print(tensor.size())
print(torch.permute(tensor, (2, 0, 1)).size())
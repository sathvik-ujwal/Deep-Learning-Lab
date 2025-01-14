import torch

b = torch.tensor(2., requires_grad=True)
x = torch.tensor(4., requires_grad=True)
w = torch.tensor(3., requires_grad=True)

u = w*x
v = u + b
a = torch.relu(v)

a.backward()

print(f"gradient da/dw: {w.grad}")
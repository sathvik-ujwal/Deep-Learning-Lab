import torch

x = torch.tensor(2., requires_grad=True)

a = x**2
b = 2*x
c = torch.sin(x)

y = -a -b -c
z = torch.exp(y)

z.backward()

print(f"dz/dx : {x.grad}")

import torch

y = torch.tensor(3., requires_grad=True)
x = torch.tensor(2., requires_grad=True)
z = torch.tensor(4., requires_grad=True)

a = 2*x
b = torch.sin(y)
c = a / b
d = c * z
e = torch.log(d + 1)
f = torch.tanh(e)

f.backward()

print(f"a: {a}\n b:{b} \n c:{c}\n d:{d}\n e:{e}\n")
print(f"df/dy: {y.grad}")
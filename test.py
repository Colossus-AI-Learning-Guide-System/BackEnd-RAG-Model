import torch
print(torch.cuda.is_available())  # Should return True
print(torch.backends.cudnn.version())  # Should return a version number

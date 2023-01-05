import torch

if torch.cuda.is_available():
    print("GPU acceleration is available")
    device = torch.cuda.current_device()
    name = torch.cuda.get_device_name(device)
    print("PyTorch is using GPU with name:", name)
else:
    print("GPU acceleration is not available")

num_gpus = torch.cuda.device_count()
print("Number of GPUs available:", num_gpus)

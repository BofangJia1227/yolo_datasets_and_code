import torch
if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f'There are {torch.cuda.device_count()} GPU(s) available.')
    print('Device name:',torch.cuda.get_device_name(0))
else:
    print('No GPU available , using the CPU instead.')
    device = torch.device("CPU")




from diffusers import StableDiffusionPipeline
import torch

# Path to model directory
project = input('Give a name to your project: ')
model_path = "./realistic_vision" # Path to huggigface stored models

if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("GPU Apple M1 (MPS)")
    pipe = StableDiffusionPipeline.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    safety_checker=None,
    requires_safety_checker=False
)

else:
    device = torch.device("cpu")
    print("CPU")
    pipe = StableDiffusionPipeline.from_pretrained(
    model_path,
    torch_dtype=torch.float32,
    safety_checker=None,
    requires_safety_checker=False
)

pipe.to(device)
# Image generator
prompt = input('Image prompt:' )
image = pipe(prompt).images[0]
# Save image to file
image.save(".outputs/" + project + "_output.png")

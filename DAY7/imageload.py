from diffusers import StableDiffusionPipeline
import torch
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-Vl-5"
)
pipe = pipe.to("CPU")
print("Success")


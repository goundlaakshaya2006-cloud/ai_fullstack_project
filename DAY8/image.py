from diffusers import StableDiffusionPipeline
import torch
pipe = StableDiffusionPipeline.from_pretrained(
    "segmind/tiny-sd",
    torch_dtype=torch.float32
)
pipe = pipe.to("cpu")
prompt = "A cute orange cat sitting in a garden. cinematic lighting, highly detailed, realistic"
image = pipe(prompt).images[0]

image.save("images/generated_image1.png")
image.show()

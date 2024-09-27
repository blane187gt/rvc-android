import subprocess, os
assets_folder = "./assets/"
if not os.path.exists(assets_folder):
    os.makedirs(assets_folder)
files = {
    "rmvpe/rmvpe.pt":"https://huggingface.co/Rejekts/project/resolve/main/rmvpe.pt",
    "hubert/hubert_base.pt":"https://huggingface.co/Rejekts/project/resolve/main/hubert_base.pt",
    "f0D32k.pth":"https://huggingface.co/lj1995/%s%s%s/resolve/main/pretrained_v2/%s" % ("Voice","Conversion","WebUI","f0D32k.pth","f0D32k.pth"),
    "f0G32k.pth":"https://huggingface.co/lj1995/%s%s%s/resolve/main/pretrained_v2/%s" % ("Voice","Conversion","WebUI","f0G32k.pth","f0G32k.pth"),
    "f0Ov2Super32kD.pth":"https://huggingface.co/lj1995/%s%s%s/resolve/main/pretrained_v2/%s" % ("Voice","Conversion","WebUI","f0Ov2Super32kD.pth","f0Ov2Super32kD.pth"),
    "f0Ov2Super32kG.pth":"https://huggingface.co/lj1995/%s%s%s/resolve/main/pretrained_v2/%s" % ("Voice","Conversion","WebUI","f0Ov2Super32kG.pth","f0Ov2Super32kG.pth"),
}
for file, link in files.items():
    file_path = os.path.join(assets_folder, file)
    if not os.path.exists(file_path):
        try:
            subprocess.run(['wget', '-nc', link, '-O', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {file}: {e}")

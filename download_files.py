import subprocess, os
assets_folder = "./assets/"
if not os.path.exists(assets_folder):
    os.makedirs(assets_folder)
files = {
    "rmvpe/rmvpe.pt": "https://huggingface.co/Rejekts/project/resolve/main/rmvpe.pt",
    "hubert/hubert_base.pt": "https://huggingface.co/Rejekts/project/resolve/main/hubert_base.pt",
    "pretrained_v2/f0D32k.pth": "https://huggingface.co/Rejekts/project/resolve/main/f0D32k.pth",
    "pretrained_v2/f0G32k.pth": "https://huggingface.co/Rejekts/project/resolve/main/f0G32k.pth",
    "pretrained_v2/f0Ov2Super32kD.pth": "https://huggingface.co/Rejekts/project/resolve/main/f0Ov2Super32kD.pth",
    "pretrained_v2/f0Ov2Super32kG.pth": "https://huggingface.co/Rejekts/project/resolve/main/f0Ov2Super32kG.pth",
    "audios/someguy.mp3": "https://huggingface.co/Rejekts/project/resolve/main/someguy.mp3",
    "audios/somegirl.mp3": "https://huggingface.co/Rejekts/project/resolve/main/somegirl.mp3",
    "audios/unchico.mp3": "https://huggingface.co/Rejekts/project/resolve/main/unchico.mp3",
    "audios/unachica.mp3": "https://huggingface.co/Rejekts/project/resolve/main/unachica.mp3"
}
for file, link in files.items():
    file_path = os.path.join(assets_folder, file)
    if not os.path.exists(file_path):
        try:
            subprocess.run(['wget', link, '-O', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {file}: {e}")

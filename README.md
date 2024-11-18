<div align="center">

<h1>RVC Android</h1>
A fork of Retrieval based Voice Conversion WebUI <br><br>

# how to install


## step 1: connect your vps
you can connect your vps by using termux with

```
pkg install openssh
```

```
ssh root@your vps id
```

## istep 2: install stuff

you can statt installing by run 
```
git clone https://github.com/blane187gt/rvc-android
cd rvc-android
```

```
pip install -r requirements-android.txt
```

```
python3 download_files.py
```

```
python3 mobile.py
```

and tthen copy the public link

## Credits
+ [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
+ [ContentVec](https://github.com/auspicious3000/contentvec/)
+ [VITS](https://github.com/jaywalnut310/vits)
+ [HIFIGAN](https://github.com/jik876/hifi-gan)
+ [Gradio](https://github.com/gradio-app/gradio)
+ [FFmpeg](https://github.com/FFmpeg/FFmpeg)
+ [Vocal pitch extraction:RMVPE](https://github.com/Dream-High/RMVPE)
+ The pretrained model is trained and tested by [yxlllc](https://github.com/yxlllc/RMVPE) and [RVC-Boss](https://github.com/RVC-Boss).

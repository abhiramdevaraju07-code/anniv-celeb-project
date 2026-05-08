import os, subprocess

PHOTOS = [
    'images/IMG_0012.jpg','images/IMG_0018.jpg','images/IMG_0037.jpg',
    'images/IMG_0118.jpg','images/IMG_0148.jpg','images/IMG_0170.jpg',
    'images/IMG_0179.jpg','images/IMG_0231.jpg','images/IMG_0234.jpg',
    'images/IMG_0241.jpg','images/IMG_0243.jpg','images/IMG_0244.jpg',
    'images/IMG_0246.jpg','images/IMG_0248.jpg','images/IMG_0250.jpg',
    'images/IMG_0251.jpg','images/IMG_0256.jpg','images/IMG_0259.jpg',
    'images/IMG_0324.jpg','images/IMG_0326.jpg','images/IMG_0332.jpg',
    'images/IMG_0341.jpg','images/IMG_0342.jpg','images/IMG_0343.jpg',
    'images/IMG_0344.jpg','images/IMG_0345.jpg','images/IMG_0346.jpg',
    'images/IMG_0359.jpg','images/IMG_0387.jpg','images/IMG_0388.jpg',
    'images/IMG_0390.jpg','images/IMG_0396.jpg','images/IMG_0397.jpg',
    'images/IMG_0410.jpg','images/IMG_0420.jpg','images/IMG_0424.jpg',
    'images/IMG_0500.jpg','images/IMG_0501.jpg','images/IMG_0502.jpg',
    'images/IMG_0503.jpg','images/IMG_0504.jpg','images/IMG_0505.jpg',
    'images/WA1.jpg','images/WA2.jpg','images/WA3.jpg',
]

# Write concat list (each photo 2 seconds so there's time to enjoy them)
with open('filelist.txt', 'w') as f:
    for p in PHOTOS:
        f.write(f"file '{p}'\nduration 2\n")
    f.write(f"file '{PHOTOS[-1]}'\n")  # final frame

subprocess.run([
    'ffmpeg', '-y',
    '-f', 'concat', '-safe', '0', '-i', 'filelist.txt',
    '-i', 'slideshow-music.mp3',
    '-vf', 'scale=1080:1080:force_original_aspect_ratio=decrease,'
           'pad=1080:1080:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1',
    '-r', '24', '-pix_fmt', 'yuv420p',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '28',
    '-c:a', 'aac_at', '-b:a', '128k',
    '-shortest',
    'slideshow-video.mp4'
], check=True)

os.remove('filelist.txt')
print("Done! slideshow-video.mp4 created.")
print(f"Size: {os.path.getsize('slideshow-video.mp4') / 1024 / 1024:.1f} MB")

#!/usr/bin/python3
# _*_ coding: UTF-8 _*_

# Created by Mario Chen, 05.04.2022, Shenzhen
# My Github site: https://github.com/Mario-Hero

import os
import sys

try:
    from mutagen.mp4 import MP4, MP4Cover
    from mutagen.id3 import APIC, ID3
except ImportError:
    os.system('pip install mutagen')
    from mutagen.mp4 import MP4, MP4Cover
    from mutagen.id3 import APIC, ID3


def changeCoverMP4(file, cover):
    if os.path.isfile(cover):
        try:
            video = MP4(file)
        except:
            print(file + ' is not mp4 file.')
            return
        with open(cover, "rb") as f:
            if cover.lower().endswith('.png'):
                video["covr"] = [MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_PNG)]
            else:
                video["covr"] = [MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)]
        video.save()


def changeCoverMP3(file, cover):
    if os.path.isfile(cover):
        music = ID3(file)  # Load the file
        music.delall("APIC")  # Delete every APIC tag (Cover art)
        music.save()  # Save the file
        if cover.lower().endswith('.png'):
            with open(cover, 'rb') as albumart:
                music.add(APIC(
                    encoding=3,
                    mime='image/png',
                    type=3, desc=u'Cover',
                    data=albumart.read()
                ))
        else:
            with open(cover, 'rb') as albumart:
                music.add(APIC(
                    encoding=3,
                    mime='image/jpeg',
                    type=3, desc=u'Cover',
                    data=albumart.read()
                ))
        music.save(v2_version=3)


def changeCover(file, cover):
    if os.path.isfile(file):
        if file.lower().endswith('.mp3'):
            changeCoverMP3(file, cover)
        elif file.lower().endswith('.mp4'):
            changeCoverMP4(file, cover)
    else:
        for child in os.listdir(file):
            changeCover(os.path.join(file, child), cover)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        pic = ''
        for file in sys.argv[1:]:
            if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.png'):
                pic = file
                break
        if pic:
            for file in sys.argv[1:]:
                if file != pic:
                    changeCover(file, pic)
    elif len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            pic = ''
            for file in os.listdir(sys.argv[1]):
                if file.startswith('cover.'):
                    pic = file
                    break
            if pic:
                for child in os.listdir(sys.argv[1]):
                    if child != pic:
                        changeCover(os.path.join(sys.argv[1], child), pic)

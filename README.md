# mp34Cover 音视频封面添加脚本

这是一个给mp3和mp4文件添加封面的Python脚本。

图片支持jpg和png格式。

This is a Python script which adds covers to MP3 and MP4 files.
Support JPG and PNG formats.

## 依赖 Dependency

Python 3

mutagen（如果没有安装，该脚本会自动安装 If not installed, the script will automatically install it.）

## 用法 Usage

把MP3或MP4文件和图片拖到脚本mp34Cover.py上，即可给文件添加封面。

把单个文件夹拖到脚本上，会在文件夹中寻找名为cover的图片作为封面。

把图片和文件夹一起拖到脚本上，会给文件夹的所有文件添加上封面，封面为选定的那张图片。

Drag MP3 or MP4 files and pictures to mp34Cover.py, you can add a cover page to the file.
Drag a single folder onto the script, it will find a picture named 'cover' in the folder as the cover.
Drag a picture and folders together onto the script, and all files in the folder will be added with a cover. The cover is the selected picture.

## License

The project is released under MIT License.
## RAW2ACES

一个重复造轮子的项目，目的是为了方便本人转 RAW 照片去 Davinci 修图  
（是的，Davinci 修图比 Lr 好用多了，还能做 HDR Plog）

### 功能 (只有一个)

调用 `RAWPY(libraw)` 将RAW照片转为 `ACES(AP0)，Linear Gamma，16-bit` 的TIFF

### 使用方法

1. `git` 本项目
2. 安装依赖库 `pip install -r requirements.txt`
3. 将 `main2.0.py` 放置在你存放 RAW 照片的文件夹中, cmd 运行 `python main2.0.py`。脚本会自动识别该目录下的 RAW
   文件，并将转换好的TIFF放在 `convert` 文件夹内。

### 代码参考及调用库

- [UltraRawConverter] https://github.com/UltraBlur/UltraRawConverter
- [RAWPY] https://github.com/letmaik/rawpy/tree/main

### 问题

- DC-S5 的 RAW 部分高光会过曝，等 `libraw` 修。
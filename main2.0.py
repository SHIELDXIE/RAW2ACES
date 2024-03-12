import os
import imageio
import rawpy

# 创建输出目录
output_dir = "./convert"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def convert_raw_to_tiff(input_path, output_dir):
    # 从输入路径获取文件名和扩展名
    filename = os.path.basename(input_path)
    filename_without_ext = os.path.splitext(filename)[0]
    output_path = os.path.join(output_dir, filename_without_ext + '.tiff')

    with rawpy.imread(input_path) as raw:
        pic = raw.postprocess(gamma=(1, 1), no_auto_bright=False, output_bps=16,
                              output_color=rawpy.ColorSpace(6),
                              fbdd_noise_reduction=rawpy.FBDDNoiseReductionMode(0),
                              highlight_mode=(2),
                              use_camera_wb=True)
        imageio.imsave(output_path, pic)
        print(f"Converted {input_path} to TIFF.")


# 获取当前目录下的所有非.py文件
for input_path in os.listdir('.'):
    if os.path.isfile(input_path) and not input_path.lower().endswith('.py'):
        convert_raw_to_tiff(input_path, output_dir)

print("done")

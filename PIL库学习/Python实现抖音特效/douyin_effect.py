# Python实现抖音特效
import copy
import argparse
import numpy as np
from PIL import Image


# 主函数
def main(imagepath):
	img = Image.open(imagepath).convert('RGBA')
	img_arr = np.array(img)
	# 提取R
	img_arr_r = copy.deepcopy(img_arr)
	img_arr_r[:, :, 1:3] = 0
	# 提取GB
	img_arr_gb = copy.deepcopy(img_arr)
	img_arr_gb[:, :, 0] = 0
	# 创建画布把图片错开放
	img_r = Image.fromarray(img_arr_r).convert('RGBA')
	img_gb = Image.fromarray(img_arr_gb).convert('RGBA')
	canvas_r = Image.new('RGB', img.size, color=(0, 0, 0))
	canvas_gb = Image.new('RGB', img.size, color=(0, 0, 0))
	canvas_r.paste(img_r, (6, 6), img_r)
	canvas_gb.paste(img_gb, (0, 0), img_gb)
	img_douyin = Image.fromarray(np.array(canvas_gb) + np.array(canvas_r))
	img_douyin.save('douyin.jpg')
	img_douyin.show()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--image', help='Image to be processed(give the file path).')
	args = parser.parse_args()
	main(args.image)
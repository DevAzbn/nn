import os

from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont

def get_watermarked(i_img, wm_img, wm_percent = 0.25):
	
	i_img_name, i_img_ext = os.path.splitext(i_img)
	# print("{} {}".format(i_img_name, i_img_ext))
	o_img = '{}_wm{}'.format(i_img_name, i_img_ext)
	o_img_webp = '{}_wm{}'.format(i_img_name, '.webp')

	pos = (0, 0)

	i = Image.open(i_img)
	wm = Image.open(wm_img)

	i_w, i_h = i.size
	wm_w, wm_h = wm.size

	wmi_w = round(i_w * wm_percent)
	wmi_h = round( wm_h * (wmi_w / wm_w) )

	wmi = wm.resize((wmi_w, wmi_h))

	wm_pos_x = round( (i_w - wmi_w) / 2 )
	wm_pos_y = round( (i_h - wmi_h) / 2 )

	wmi_pos = (wm_pos_x, wm_pos_y)

	transparent = Image.new('RGBA', (i_w, i_h), (0, 0, 0, 0))
	transparent.paste(i, pos)
	transparent.paste(wmi, wmi_pos, mask=wmi)
	if ( i_img.endswith('.jpg') or i_img.endswith('.jpeg') or i_img.endswith('.JPG') or i_img.endswith('.JPEG') ):
		transparent = transparent.convert('RGB')
	# transparent.show()
	transparent.save(o_img)
	transparent.save(o_img_webp, 'WEBP')

	return o_img


def get_resized(i_img, wsize, crop):
	
	i_img_dname = os.path.dirname(i_img)
	i_img_name, i_img_ext = os.path.splitext(i_img)
	
	i = Image.open(i_img)
	i_w, i_h = i.size
	pc = i_w / i_h

	hsize = round(wsize / pc)

	o_img = '{}/{}_{}_rs{}'.format(i_img_dname, wsize, hsize, i_img_ext)

	# rs = i.resize((wsize, hsize))
	# rs.save(o_img)

	i.thumbnail((wsize, hsize))
	i.save(o_img)

	return o_img



if __name__ == '__main__':
	image_wm = './watermark.png'
	image_src = './../../image/watermark/origin.png'

	wm = get_watermarked(image_src, image_wm)
	get_resized(wm, 300, True)

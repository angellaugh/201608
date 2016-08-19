# -*- coding=utf-8 -*-

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s:%s' %(k,v))
	print('Data:',data.decode('utf-8'))

from PIL import Image

# im = Image.open('test.jpg')

# w,h = im.size
# print('Original image size:%sx%s' % (w,h))

# im.thumbnail((w//2,h//2)

# print('Resize image to: %sx%s' % (w//2,h//2))
# im.save('thumbnail.jpg','jpeg')

im = Image.open('test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')


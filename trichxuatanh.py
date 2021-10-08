import cv2
import os

cam = cv2.VideoCapture('D:\\xu ly anh\\Pexels Videos 2802070.mp4')

# tạo 1 tệp có tên là data, nếu không tạo được thì in ra lỗi 

try:
	if not os.path.exists('data'):
		os.makedirs('data')

except OSError:
	print('Error: Creating directory of data')

currentframe = 0
while True:
	ret, frame = cam.read()

	if ret:
		#tạo hình ảnh cho đến khi hết video
		name = './data/frame' + str(currentframe) + '.jpg'
		print('Creating...' + name)

		#lưu các hình ảnh trích xuất
		cv2.imwrite(name, frame) 

		#tăng bộ đếm và hiển thì xem có bao nhiêu khung hình được tạo
		currentframe += 1

	else:
		break

cam.release()
cv2.destroyAllWindows()
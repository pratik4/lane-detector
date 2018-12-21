import cv2 as cv
# from matplotlib import pyplot as plt
import numpy as np

cap = cv.VideoCapture('input.mp4')


def do_canny(frame):

	gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

	blur = cv.GaussianBlur(gray, (5,5), 0)

	canny = cv.Canny(blur, 50, 150)

	return canny



def do_segment(frame):

	height = frame.shape[0]

	polygons = np.array([
							[(0, height), (800, height), (380,290)]
						])

	mask = np.zeros_like(frame)

	cv.fillPoly(mask, polygons, 255)

	segment = cv.bitwise_and(frame, mask)

	return segment



while( cap.isOpened()):
	ret, frame = cap.read()

	canny = do_canny(frame)

	segment = do_segment(canny)

	cv.imshow('frame', segment)


	if cv.waitKey(10) & 0xFF == ord('q'):
		break

	hough = cv.HoughLinesP(segment, 2, np.pi / 180, 100, np.array([]), minLineLength = 100, maxLineGap = 50)




cap.release()
cv.destroyAllWindoes()



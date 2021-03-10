from post import posteriz
from conv_canny import*
import timeit

#posteriz("puppy.jpg", 5)

# cv::IMREAD_UNCHANGED = -1,
# cv::IMREAD_GRAYSCALE = 0,
# cv::IMREAD_COLOR = 1,

#img = cv.imread('poster.jpg', 0)
img = cv.imread('puppy.jpg', 0)
start = timeit.default_timer()

print_edges_contours(img)

stop = timeit.default_timer()

print('Time: ', stop - start)

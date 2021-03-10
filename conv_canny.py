import post
import cv2 as cv
import numpy as np

def create_canvas(img):
    shape = list(img.shape)
    canvas = np.zeros(shape,dtype=np.uint8)
    canvas.fill(255)
    return canvas

def print_edges_contours(img):
    #CANNY steps for edges:
    #Smoothing noise, fine texture (Gaussian Smoothing)
    #Fit a curve to the light and dark gradient (partial derivatives)
    #non-maximum suppression: ignore pixels that are too far.
    #Double thresholding

    canvas = create_canvas(img)

    blurred_img = cv.GaussianBlur(img, (3,3), 1, 1)
    #Canny(InputArray image, OutputArray edges,
    #double threshold1, double threshold2, int apertureSize = 3,bool L2gradient = false )
    #https://stackoverflow.com/questions/63543033/does-cv2-canny-perform-a-gaussian-blur
    edges = cv.Canny(blurred_img,100,170)
    contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    img_w_cntrs = cv.drawContours(canvas, contours, -1, (0,255,0), 1)

    cv.imwrite('blurred.jpg', blurred_img)

    cv.imwrite('gray_scale.jpg', img)

    cv.imwrite('edge_image.jpg', edges)

    cv.imwrite('contours_image.jpg', img_w_cntrs)

    return

import posterize
import matplotlib.pyplot as plt
import cv2 as cv

def print_edges_contours(img):
    img_copy = img.copy()

    #CANNY steps for edges:
    #Smoothing noise, fine texture (Gaussian Smoothing)
    #Fit a curve to the light and dark gradient (partial derivatives)
    #non-maximum suppression: ignore pixels that are too far.
    #Double thresholding

    #Canny(InputArray image, OutputArray edges,
    #double threshold1, double threshold2, int apertureSize = 3,bool L2gradient = false )
    edges = cv.Canny(img,100,200)
    contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cont = cv.drawContours(img_copy, contours, -1, (0,255,0), 1)

    cv.imwrite('gray_scale.jpg', img)

    cv.imwrite('edge_image.jpg', edges)

    cv.imwrite('contours_image.jpg', cont)

    return

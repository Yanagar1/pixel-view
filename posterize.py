from PIL import Image
from sklearn.cluster import KMeans #Kmeans: Minimize tot sq distance(data to centeroid)
import numpy as np


def img_to_px_array(loaded_img, width, height):
    list_of_pix = []
    for row in range(height):   #y
        for column in range(width):  #x
            list_of_pix.append(list(loaded_img[column, row]))
    X = np.array(list_of_pix)
    return X

#Now find 3 most popular colors
def sklearn_kmeans(X, p):
    kmeans = KMeans(n_clusters = p)
    inds = kmeans.fit_predict(X) #list of cluster indeces
    key_colors=[] #list of tuples rgb
    for i in range(p):
        key_color = kmeans.cluster_centers_[i]
        key_color = tuple(key_color.astype(np.int64))
        key_colors.append(key_color)
    return key_colors, inds

def replace_colors(pix, key_colors_list, ind_per_px, width, height):
    for y in range(height):
        for x in range(width):
            pix_loc = (y*width)+x
            corr_new_color_ind = int(ind_per_px[pix_loc])
            pix[x, y] = key_colors_list[corr_new_color_ind]
    return pix

def posterize(file_name, p):
    my_image = Image.open(file_name, mode="r")
    width, height = my_image.size #tot 189744
    img_out = my_image.copy()
    pix = img_out.load()         #pix[x,y] = (r, g, b) //tuple
    X = img_to_px_array(pix, width, height)
    kmeans_out_tuple = sklearn_kmeans(X, p)
    replace_colors(pix, kmeans_out_tuple[0], kmeans_out_tuple[1], width, height)
    img_out.save("poster.jpg")
    return
    

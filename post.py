import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans #Kmeans: Minimize tot sq distance(data to centeroid)
from sklearn.utils import shuffle
#https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans.fit_predict


def sklearn_kmeans(my_image_array, p):
    array_sample = shuffle(my_image_array, random_state=0)[:1000]
    kmeans = KMeans(n_clusters = p, random_state=0).fit(array_sample)
    inds = kmeans.predict(my_image_array) #index of cluster each pixel belongs to
    key_colors=[] #list of tuples rgb
    for i in range(p):
        key_color = tuple((kmeans.cluster_centers_[i]).astype(np.int64))
        key_colors.append(key_color)
    return key_colors, inds

def form_picture(key_colors, ind_per_px, width, height, channels):
    img_out = np.zeros((width, height, channels))
    pix_loc = 0
    for x in range(width):
        for y in range(height):
            corr_new_color_ind = int(ind_per_px[pix_loc])
            img_out[x, y] = key_colors[corr_new_color_ind]
            pix_loc+=1
    return img_out

def posteriz(file_name, p):
    my_image = np.array(cv.imread(file_name))
    width, height, channels = tuple(my_image.shape)
    my_image_array = np.reshape(my_image, (width * height, channels))
    #print(len(my_image_array))
    kmeans_out_tuple = sklearn_kmeans(my_image_array, p)
    #print(kmeans_out_tuple)
    img_out = form_picture(kmeans_out_tuple[0], kmeans_out_tuple[1], width, height, channels)
    cv.imwrite("poster.jpg", img_out)
    return

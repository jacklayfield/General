import numpy as np
import json
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import sys


def chip_image(img, coords, classes, shape=(300, 300)):
    """
    Chip an image and get relative coordinates and classes.  Bounding boxes that pass into
        multiple chips are clipped: each portion that is in a chip is labeled. For example,
        half a building will be labeled if it is cut off in a chip. If there are no boxes,
        the boxes array will be [[0,0,0,0]] and classes [0].
        Note: This chip_image method is only tested on xView data-- there are some image manipulations that can mess up different images.

    Args:
        img: the image to be chipped in array format
        coords: an (N,4) array of bounding box coordinates for that image
        classes: an (N,1) array of classes for each bounding box
        shape: an (W,H) tuple indicating width and height of chips

    Output:
        An image array of shape (M,W,H,C), where M is the number of chips,
        W and H are the dimensions of the image, and C is the number of color
        channels.  Also returns boxes and classes dictionaries for each corresponding chip.
    """
    height, width, _ = img.shape

    print("height/width: ", height, " -- ", width, "\n")
    wn, hn = shape

    print("wn/hn: ", wn, " -- ", hn, "\n")

    w_num, h_num = (int(width/wn), int(height/hn))

    print("w_num, h_num: ", w_num, " -- ", h_num, "\n")

    images = np.zeros((w_num*h_num, hn, wn, 3))
    total_boxes = {}
    total_classes = {}

    k = 0
    for i in range(w_num):
        for j in range(h_num):
            x = np.logical_or(np.logical_and((coords[:, 0] < ((i+1)*wn)), (coords[:, 0] > (i*wn))),
                              np.logical_and((coords[:, 2] < ((i+1)*wn)), (coords[:, 2] > (i*wn))))

            out = coords[x]

          #  print("x: ", x)
           # print("x coords: ", out, "\n")

            y = np.logical_or(np.logical_and((out[:, 1] < ((j+1)*hn)), (out[:, 1] > (j*hn))),
                              np.logical_and((out[:, 3] < ((j+1)*hn)), (out[:, 3] > (j*hn))))
            outn = out[y]

         #   print("y: ", y)
          #  print("y coords: ", outn, "\n")
            out = np.transpose(np.vstack((np.clip(outn[:, 0]-(wn*i), 0, wn),
                                          np.clip(outn[:, 1]-(hn*j), 0, hn),
                                          np.clip(outn[:, 2]-(wn*i), 0, wn),
                                          np.clip(outn[:, 3]-(hn*j), 0, hn))))
            box_classes = classes[x][y]

          #  print("box classes: ", box_classes, "\n")

            if out.shape[0] != 0:
                total_boxes[k] = out
                total_classes[k] = box_classes
            else:
                total_boxes[k] = np.array([[0, 0, 0, 0]])
                total_classes[k] = np.array([0])

            chip = img[hn*j:hn*(j+1), wn*i:wn*(i+1), :3]
            images[k] = chip

            k = k + 1

    return images.astype(np.uint8), total_boxes, total_classes


with open('xView_train.geojson') as f:
    data = json.load(f)

numb_features = len(data['features'])

img_ids = np.zeros(numb_features, dtype="object")
coords = np.zeros((numb_features, 4))
classes = np.zeros(numb_features)

# Process every feature obj
for i in range(numb_features):
    if data['features'][i]['properties']['bounds_imcoords'] != []:
        img_ids[i] = data['features'][i]['properties']['image_id']
        coords[i] = np.array([int(num) for num in data['features']
                              [i]['properties']['bounds_imcoords'].split(",")])
        classes[i] = data['features'][i]['properties']['type_id']


print("COORDINATES: ", coords, "\n\n\n")
print("img ids: ", img_ids, "\n\n\n")
print("classes: ", classes, "\n\n\n")

# with np.printoptions(threshold=np.inf):
#     print(img_ids)

print("img ids: ", img_ids)
img_id = img_ids[3000]

print("len   : ", len(classes))

print("img_id: ", img_id)

coords = coords[img_ids == img_id]
classes = classes[img_ids == img_id].astype(np.int64)


img = np.array(Image.open("./train_images/" + img_id))

plt.figure(figsize=(12, 12))
plt.axis('off')
plt.imshow(img)
plt.show()


# c_img, c_box, c_cls = chip_image(
#     img=img, coords=coords, classes=classes, shape=(500, 500))

# ind = np.random.choice(range(c_img.shape[0]))

###################################
###################################

total_boxes = {}
total_classes = {}

height, width, _ = img.shape

x = np.logical_or(np.logical_and((coords[:, 0] < (width)), (coords[:, 0] > (width))),
                  np.logical_and((coords[:, 2] < (width)), (coords[:, 2] > (width))))

out = coords[x]

print("x: ", x)
print("x coords: ", out, "\n")

y = np.logical_or(np.logical_and((out[:, 1] < (height)), (out[:, 1] > (height))),
                  np.logical_and((out[:, 3] < (height)), (out[:, 3] > (height))))
outn = out[y]

print("y: ", y)
print("y coords: ", outn, "\n")
out = np.transpose(np.vstack((np.clip(outn[:, 0]-(width), 0, width),
                              np.clip(outn[:, 1]-(height), 0, height),
                              np.clip(outn[:, 2]-(width), 0, width),
                              np.clip(outn[:, 3]-(height), 0, height))))
box_classes = classes[x][y]

print("box classes: ", box_classes, "\n")

if out.shape[0] != 0:
    total_boxes[0] = out
    total_classes[0] = box_classes
else:
    total_boxes[0] = np.array([[0, 0, 0, 0]])
    total_classes[0] = np.array([0])


###################################
###################################

# Draw boxes
source = Image.fromarray(img)
draw = ImageDraw.Draw(source)
w2, h2 = (img.shape[0], img.shape[1])

idx = 0

print(total_boxes[0])

for b in total_boxes[0]:
    xmin, ymin, xmax, ymax = b

    for j in range(3):
        draw.rectangle(((xmin+j, ymin+j), (xmax+j, ymax+j)), outline="red")


plt.figure(figsize=(5, 5))
plt.axis('off')
plt.imshow(source)
plt.show()

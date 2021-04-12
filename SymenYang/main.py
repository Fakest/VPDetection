
import wrapper
import os
import cv2

inpath = "./data/"
outpath = "./result/"

entries = os.listdir(inpath)
for entry in entries:
    if not os.path.isdir(os.path.join(inpath, entry)):
        continue
    image_file_name = os.path.join(inpath + entry, '%s.%s' % (entry, "jpg"))
    output = os.path.join(outpath, entry)
    wrapper.dealAImage(image_file_name, output, True, True, True)


# for image_path in os.listdir(inpath):
#     if image_path.endswith(".jpg"):
#         img = os.path.abspath(os.path.join(inpath, image_path))
#         print(img)
#         output = os.path.join(outpath, image_path)
#         wrapper.dealAImage(img, output, True, True, True)

# for i in range(1,14,1):
#     wrapper.dealAImage("data/" + str(i),"data/result/" + str(i),True,True,True)
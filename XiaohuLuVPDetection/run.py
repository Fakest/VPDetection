import os
import cv2
import time
from lu_vp_detect import VPDetection

length_thresh = 60
principal_point = None
focal_length = 1500
seed = 1337


IMAGE_EXTENSION = 'jpg'
# Pixel dimensions of the images in the dataset.
IMAGE_DIMS = (640, 480)

outpath = "lu_vp_detect/results/YorkUrbanDB/"
inpath = "lu_vp_detect/data/YorkUrbanDB/"

def load_dataset(dataset_path):
    """Loads the York Urban vanishing point dataset.

    Args:
        dataset_path: String, path to a directory.
        show_progress_bar: Boolean, whether to print a progress bar.

    Returns:
        Dataset instance.
    """
    image_paths = []
    # Images paths are <base>/<base>.jpg.
    # VP data paths are <base>/<base>LinesAndVP.mat.
    entries = os.listdir(dataset_path)
    for entry in entries:
        if not os.path.isdir(os.path.join(dataset_path, entry)):
            continue
        image_file_name = os.path.join(entry, '%s.%s' % (entry, IMAGE_EXTENSION))
        image_paths.append(os.path.join(dataset_path, image_file_name))

    return image_paths

#for image_path in os.listdir(inpath):
#    if(image_path.endswith(".jpg")):
image_paths = load_dataset("lu_vp_detect/data/YorkUrbanDB")
for image in image_paths:
    start = time.process_time()
    vpd = VPDetection(length_thresh, principal_point, focal_length, seed)
    vpd.find_vps(image)
    vps2d = vpd.vps_2D
    final = time.process_time()
    print(f'img : {image} VPS : {vps2d} time : {final - start}')
    img = vpd.create_debug_VP_image(show_vp=True)
    ans = open(outpath + image[-12:-4] + ".txt", 'a')
    ans.write(f'VPs : {str(vps2d)}, time : {str(final - start)}')
    ans.close()
    cv2.imwrite(outpath + image[-12:-4] + ".jpg", img)



# for i in range(size):
#     img = "test_image.jpg"
#     vpd = VPDetection(length_thresh, principal_point, focal_length, seed)
#     vpd.find_vps(img)
#     vps2d = vpd.vps_2D
#     img = vpd.create_debug_VP_image(show_vp=True)
#     cv2.imwrite("lu_vp_detect/results/result.jpg", img)

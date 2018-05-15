import time
from img_download_info import IMG_DOWNLOAD_INFO

class DownloadResizeImagesService(object):
    def __init__(self, img_dl_time_dict):
        self._img_dl_time_dict = img_dl_time_dict

    def _download_image(self, img_id, dl_time):
        print("[download_image]Start: download {}".format(img_id))
        start = time.perf_counter()

        time.sleep(dl_time)
        
        end = time.perf_counter()
        print("[download_image]End: downloaded {} in {} seconds".format(img_id, end - start))

    def download_images(self):        
        print("[download_images]Start: -----------")
        start = time.perf_counter()

        for img_id, dl_time in self._img_dl_time_dict.items():
            self._download_image(img_id, dl_time)
        
        end = time.perf_counter()
        print("[download_images]End: downloaded {} images in {} seconds".format(len(self._img_dl_time_dict), end - start))

    def resize_images(self):
        print("[resize_images]Start: -----------")
        start = time.perf_counter()

        for _ in range(len(self._img_dl_time_dict)):
            # 假设每个img的resize只要0.1秒
            time.sleep(0.1)

        end = time.perf_counter()
        print("[resize_images]End: resized {} images in {} seconds".format(len(self._img_dl_time_dict), end - start))

    def download_resize_images(self):
        print("[download_resize_images]Start: =============")
        start = time.perf_counter()

        self.download_images()
        self.resize_images()

        end = time.perf_counter()
        print("[download_resize_images]End: download_resize_images in {} seconds".format(end - start))


service = DownloadResizeImagesService(IMG_DOWNLOAD_INFO)
service.download_resize_images()

"""
[download_images]Start: -----------
[download_image]Start: download img1
[download_image]End: downloaded img1 in 1.0068449040291214 seconds
[download_image]Start: download img2
[download_image]End: downloaded img2 in 2.0007191342965065 seconds
[download_image]Start: download img3
[download_image]End: downloaded img3 in 3.004157996576454 seconds
[download_image]Start: download img4
[download_image]End: downloaded img4 in 4.003155511697602 seconds
[download_image]Start: download img5
[download_image]End: downloaded img5 in 4.998679520645208 seconds
[download_image]Start: download img6
[download_image]End: downloaded img6 in 6.006236630192117 seconds
[download_images]End: downloaded 6 images in 21.035620122048613 seconds
[resize_images]Start: -----------
[resize_images]End: resized 6 images in 0.653199308872555 seconds
[download_resize_images]End: download_resize_images in 21.692753883215797 seconds
"""

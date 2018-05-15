import time
from threading import Thread
from img_download_info import IMG_DOWNLOAD_INFO

class DownloadResizeImagesService(object):
    def __init__(self, img_dl_time_dict):
        self._img_dl_time_dict = img_dl_time_dict
        self._total_downloaded_bytes = 0 # !!!!演示lock

    def _download_image(self, img_id, dl_time):
        print("[download_image]Start: download {}".format(img_id))
        start = time.perf_counter()

        time.sleep(dl_time)
        self._total_downloaded_bytes += 1000 # 假设每个img都是1000 byte大小
        
        end = time.perf_counter()
        print("[download_image]End: downloaded {} in {} seconds".format(img_id, end - start))

    def download_images(self):        
        print("[download_images]Start: -----------")
        start = time.perf_counter()

        dl_threads = []

        for img_id, dl_time in self._img_dl_time_dict.items():
            t = Thread(target=self._download_image, args=(img_id, dl_time))
            t.start() 
            dl_threads.append(t)
        
        for t in dl_threads: 
            t.join() 

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
print("private __total_downloaded_bytes: " + str(service._total_downloaded_bytes))

import time
from threading import Thread, Lock, Semaphore
from img_download_info import IMG_DOWNLOAD_INFO

class DownloadResizeImagesService(object):
    MAX_CONCURRENT_DL = 2

    def __init__(self, img_dl_time_dict):
        self._img_dl_time_dict = img_dl_time_dict
        self._total_downloaded_bytes = 0 # !!!!演示lock
        self._total_downloaded_bytes_lock = Lock() # !!!!演示lock
        self._max_concurrent_dl_thread_num_semaphore = Semaphore(self.MAX_CONCURRENT_DL) # !!!!演示Semaphor        

    def _download_image(self, img_id, dl_time):
        with self._max_concurrent_dl_thread_num_semaphore:  # No more than 2 threads can exe the download_code at the same time!
            print("[download_image]Start: download {}".format(img_id))
            start = time.perf_counter()

            time.sleep(dl_time)
            
            with self._total_downloaded_bytes_lock: # 保证with里面的变量不会被多个子线程一起占用。一个问题： 共享变量什么时候用lock，什么时候可以不用？
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


"""
[download_resize_images]Start: =============
[download_images]Start: -----------
[download_image]Start: download img1
[download_image]Start: download img2
[download_image]End: downloaded img1 in 1.0010108723478275 seconds
[download_image]Start: download img3
[download_image]End: downloaded img2 in 2.0077828418641186 seconds
[download_image]Start: download img4
[download_image]End: downloaded img3 in 3.0080603576854377 seconds
[download_image]Start: download img5
[download_image]End: downloaded img4 in 4.014196702922412 seconds
[download_image]Start: download img6
[download_image]End: downloaded img5 in 5.000676102933937 seconds
[download_image]End: downloaded img6 in 6.003220058741456 seconds
[download_images]End: downloaded 6 images in 12.042878200092918 seconds
[resize_images]Start: -----------
[resize_images]End: resized 6 images in 0.6126400616150764 seconds
[download_resize_images]End: download_resize_images in 12.661666276467024 seconds
private __total_downloaded_bytes: 6000
"""
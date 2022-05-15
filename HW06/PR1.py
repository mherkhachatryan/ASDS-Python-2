from abc import ABC, abstractmethod
import time
import tqdm


class ImageDBBase(ABC):
    def __init__(self):
        self._request_time = 30

    @abstractmethod
    def request(self, num_images):
        pass


class ImageDB(ImageDBBase):

    def request(self, num_images):
        print(f"Requested {num_images} images, loading...")

        for _ in tqdm.tqdm(range(self._request_time), desc="Image loading"):
            time.sleep(1 / self._request_time)
        print("Connection timed out.... ")
        return None


class ProxyImageDB(ImageDBBase):
    def __init__(self, image_db):
        super().__init__()
        self._image_db = image_db
        self._cached_images = ["lenna.png"]

    def request(self, num_images):
        if self._wait_time_exceed():
            print("Wait time exceeded returning cached images")
            return self._pad_or_truncate(self._cached_images, num_images)

    def _wait_time_exceed(self):
        for _ in tqdm.tqdm(range(self._request_time), desc="Image loading"):
            time.sleep(1 / self._request_time)
        if self._request_time > 10:
            return True
        else:
            return False

    def _pad_or_truncate(self, some_list, target_len):
        return some_list[:target_len] + some_list * (target_len - len(some_list))


def client_code(image_request, num_images):
    return image_request.request(num_images)


if __name__ == "__main__":
    image_database = ImageDB()

    images = client_code(image_database, 10)
    print(images)

    print("\nNow with proxy\n")

    proxy = ProxyImageDB(image_database)

    images_proxy = client_code(proxy, 10)
    print(images_proxy)

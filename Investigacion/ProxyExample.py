class Image:
    def __init__(self, filename):
        self.filename = filename
        self.is_loaded = False
        self.image_data = None

        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Cargando {self.filename}...")
        self.image_data = open(self.filename, "rb").read()
        self.is_loaded = True

    def display_image(self):
        if not self.is_loaded:
            self.load_image_from_disk()

        print(f"Mostrando {self.filename}")
        # código para mostrar la imagen


class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.image = None
        self.is_loaded = False

    def display_image(self):
        if not self.is_loaded:
            self.image = Image(self.filename)
            self.is_loaded = True

        self.image.display_image()


if __name__ == "__main__":
    proxy_image1 = ProxyImage("image1.png")
    proxy_image1.display_image()

    proxy_image2 = ProxyImage("image2.png")
    proxy_image2.display_image()

    proxy_image1.display_image()

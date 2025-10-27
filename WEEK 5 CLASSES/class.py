# Base Class
class Device:
    def __init__(self, brand, model):
        self._brand = brand        # Protected attribute (Encapsulation)
        self._model = model

    def device_info(self):
        return f"Brand: {self._brand}, Model: {self._model}"

# Derived Class
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)   # Inherit base class attributes
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"📸 Taking a {self.camera_megapixels}MP photo...")

    def make_call(self, contact_name):
        print(f"📞 Calling {contact_name} from your {self._brand} {self._model}...")

    def phone_specs(self):
        return (f"Smartphone Specs:\n"
                f"Brand: {self._brand}\n"
                f"Model: {self._model}\n"
                f"Storage: {self.storage}GB\n"
                f"Camera: {self.camera_megapixels}MP")

# Example Usage
phone1 = Smartphone("Apple", "iPhone 15 Pro", 256, 48)
phone2 = Smartphone("Samsung", "Galaxy S24 Ultra", 512, 200)

print(phone1.phone_specs())
phone1.take_photo()
phone2.make_call("Loren")

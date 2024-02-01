class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = f"Файл {args} поврежден"
        else:
            self.message = f"Файл поврежден"

    def __str__(self):
        return self.message

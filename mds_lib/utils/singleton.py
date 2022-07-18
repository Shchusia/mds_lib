class Singleton:
    """
    Class implements the singleton pattern
    Example:
        @Singleton
        class Example:
    """

    def __init__(self, class_):
        self.class_ = class_
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self.class_(*args, **kwargs)
        return self._instance

import logging
import threading


class MySingleton(object):
    _instance: object = None
    _lock: threading.Lock = threading.Lock()

    # Используйте self для первого аргумента для методов экземпляра.
    # Используйте cls для первого аргумента для методов класса.

    def __new__(cls):
        """Create a new instance"""
        if MySingleton._instance is None:
            with MySingleton._lock:
                if MySingleton._instance is None:
                    MySingleton._instance = super(MySingleton, cls).__new__(cls)
                    MySingleton._instance._initialized = False

        return MySingleton._instance

    def __init__(self):
        """Initialize the instance"""
        if self._initialized is False:
            self._logger = logging.getLogger(self.__class__.__name__)
            self._count = 0

            self._initialized = True

        self._logger.debug("using instance: %s" % self._instance)

    def increment(self):
        """Increment the counter"""
        self._count += 1
        self._logger.debug("count = %d" % self._count)

if  __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
    a = MySingleton()
    b = MySingleton()
    a.increment()
    a.increment()
    b.increment()
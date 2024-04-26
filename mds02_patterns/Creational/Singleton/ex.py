from dataclasses import dataclass


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


@dataclass
class Settings(metaclass=SingletonMeta):
    db: str = "MySQL"
    host: str = "localhost"
    port: int = 5432


if __name__ == "__main__":
    settings1 = Settings()
    settings2 = Settings()
    print(settings1 is settings2)
    settings1.db = "SQLite"
    print(settings2.db)

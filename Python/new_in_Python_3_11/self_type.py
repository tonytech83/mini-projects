from typing import Self


class Language:

    def __init__(self, name, version, release_date):
        self.name = name
        self.version = version
        self.release_date = release_date

    def change_version(self, version) -> Self:
        self.version = version
        return Language(self.name, self.version, self.release_date)


lang = Language('Python', 3.11, 'November')
lang.change_version(3.12)
print(lang.version)

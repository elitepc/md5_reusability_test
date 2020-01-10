import hashlib


class OurMd5:
    static_string = 'INITIAL_TEST'

    def __init__(self):
        pass

    @staticmethod
    def _sha1(fname):
        hash_md5 = hashlib.sha1()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def _md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def fixed_string_before(file_location):
        hash_md5 = hashlib.md5()
        hash_md5.update(str.encode(OurMd5.static_string))

        with open(file_location, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()

    @staticmethod
    def fixed_string_middle(file_location):
        hash_md5 = hashlib.md5()

        with open(file_location, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(str.encode(OurMd5.static_string))
                hash_md5.update(chunk)

        return hash_md5.hexdigest()

    @staticmethod
    def fixed_string_after(file_location):
        hash_md5 = hashlib.md5()

        with open(file_location, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        hash_md5.update(str.encode(OurMd5.static_string))

        return hash_md5.hexdigest()

    @staticmethod
    def sha1_before(file_location):
        precomputed_sha1 = OurMd5._sha1(file_location)
        hash_md5 = hashlib.md5()
        hash_md5.update(str.encode(precomputed_sha1))

        with open(file_location, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()

    @staticmethod
    def sha1_middle(file_location):
        precomputed_sha1 = OurMd5._sha1(file_location)
        hash_md5 = hashlib.md5()

        with open(file_location, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(str.encode(precomputed_sha1))
                hash_md5.update(chunk)

        return hash_md5.hexdigest()

    @staticmethod
    def sha1_after(file_location):
        precomputed_sha1 = OurMd5._sha1(file_location)
        hash_md5 = hashlib.md5()

        with open(file_location, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        hash_md5.update(str.encode(precomputed_sha1))

        return hash_md5.hexdigest()

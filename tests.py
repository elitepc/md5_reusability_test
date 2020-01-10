import hashlib
from datetime import datetime

from our_md5 import OurMd5

file1 = 'test_files/generated_test_files/IPLeiria_msg1.png'
file2 = 'test_files/generated_test_files/IPLeiria_msg2.png'


def many_rounds(fname1, fname2, hash_function):
    csv_file = open("tests_log.csv", "a+")
    log_file = open("tests_log.txt", "a+")
    log_file.write(":::::::::::::::::::::::::::::::::::::::::::::::: \r\n")
    log_file.write("%s: \r\n" % hash_function.__name__)
    for name in [fname1, fname2]:
        log_file.write("  %s: \r\n" % name)
        csv_file.write("%s" % hash_function.__name__)
        csv_file.write(";%s:" % name)
        start_time = datetime.now()
        hash_result = ''
        for i in range(1, 1000000):
            hash_result = hash_function(name)
        final_time = str(datetime.now() - start_time)
        log_file.write("    Resulting hash: %s\r\n" % hash_result)
        log_file.write("    Time taken: %s\r\n" % final_time)
        csv_file.write(";%s" % hash_result)
        csv_file.write(";%s\n" % final_time)
    log_file.write(":::::::::::::::::::::::::::::::::::::::::::::::: \r\n")
    log_file.close()
    csv_file.close()


functions_to_test = [
    OurMd5.fixed_string_before,
    OurMd5.fixed_string_middle,
    OurMd5.fixed_string_after,
    OurMd5.sha1_before,
    OurMd5.sha1_middle,
    OurMd5.sha1_after
]

csv_file = open("tests_log.csv", "w")
csv_file.write("hash_function;file_name;hash_result;time_taken\n")
csv_file.close()
for function_to_test in functions_to_test:
    many_rounds(
        file1,
        file2,
        function_to_test
    )

# startTime = datetime.now()
# for i in range(1,100000):
#     md5('old/download_msg1.jpg')
#     md5('old/download_msg2.jpg')
#     md5('download.jpg')
#
# print(datetime.now() - startTime)
"""
startTime = datetime.now()
for i in range(1,100000):
    ourMD5('old/download_msg1.jpg')
    ourMD5('old/download_msg2.jpg')
    ourMD5('download.jpg')
 
print(datetime.now() - startTime)
"""
# print(sha1('old/download_msg1.jpg'))
# print(sha1('old/download_msg2.jpg'))
# print(sha1('download.jpg'))
# print('nosso')
# print('ourmd5 ' + ourMD5('old/download_msg1.jpg'))
# print('ourmd5 ' + ourMD5('old/download_msg2.jpg'))
# print(ourMD5('download.jpg'))


"""
def sha1(fname):
    hash_md5 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def ourMD5(fname, current_string):
    # first_md5 = md5(fname)
    # print('filename ' + fname)
    hash_md5 = hashlib.md5()

    with open(fname, "rb") as f:
        # print('md5: ' + first_md5)
        hash_md5.update(str.encode(current_string))
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def many_rounds(fname1, fname2):
    current_string = ''
    for i in range(1, 40960):
        current_string = current_string + 'a'
        md51 = ourMD5(fname1, current_string)
        md52 = ourMD5(fname2, current_string)
        if md51 == md52:
            print('success')
            print('current_string ' + current_string)
            print('md5 result ' + md51)
            print('i ' + str(i))


"""

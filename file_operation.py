# file objects:

# with open("test.txt", "r") as f:
#     file_content = f.read()
#     print(file_content)

# with open("test.txt", "r") as f:
#     read_char = 30
#     file_content = f.read(read_char)
#     while len(file_content) > 0:
#         print(file_content, end="*$")
#         file_content = f.read(read_char)

# from here Writing of file begins

# with open("test_write.txt", "w") as f:
#     # file_write = f.write("test_write.txt")
#     f_holder = f.write("My Test File Through Python")
#     f.write(" My another quotation")

# with open("test.txt", "r") as rf:
#     with open("test_copy", "w") as wf:
#         for line in rf:
#             wf.write(line)

with open("test.txt", "r") as rf:
    with open("test_while.txt", "w") as wf:
        chunk_size = 30
        reading = rf.read(chunk_size)
        while len(reading) > 0:
            wf.write(reading)
            reading = rf.read(chunk_size)

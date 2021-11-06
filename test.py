def check_str():
    s = "xin chao tat ca moi nguoi"
    words = ["xin", "tat", "anh", "em", "xin chao"]
    result = []
    for word in words:
        if s.__contains__(word):
            result.append(word)
    print(result)

check_str()

# a = "to write with (a pen): viết bằng (bút)"
# p = a.split(":")
#
# dicto = {}
#
#
# def Convert(a):
#     it = iter(a)
#     res_dct = dict(zip(it, it))
#     return res_dct
#
#
# print(Convert(p))
# # print(p)


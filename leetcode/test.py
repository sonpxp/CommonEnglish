# a = "to write with (a pen): viết bằng (bút)"
# p = a.split(":")
#
# dicto = {}
#
# convert list[] to dict {}
# def Convert(a):
#     it = iter(a)
#     res_dct = dict(zip(it, it))
#     return res_dct
#
#
# print(Convert(p))
# # print(p)


# def check_str():
#     s = "xin chao tat ca moi nguoi"
#     words = ["xin", "tat", "anh", "em", "xin chao"]
#     result = []
#     for word in words:
#         if s.__contains__(word):
#             result.append(word)
#     print(f"check: {result}")
#
#
# check_str()


# def check_str2():
#     str = "xin chao tat ca moi nguoi"
#     words = ["xin", "tat", "anh", "em", "xin chao"]
#     matches = []
#     for x in words:
#         if x in str:
#             matches.append(x)
#     print(f"check-2: {matches}")
#
#
# check_str2()


def check_str3(allowed: str, words: []) -> []:
    map_allowed = list(map(str, allowed))
    map_words = list(map(str, words))
    di = []

    print(map_allowed)
    print(map_words)


strings = "xin chao tat ca moi nguoi"
words = ["xin", "tat", "anh", "em", "xin chao"]


# print(check_str3(strings, words))

######################################


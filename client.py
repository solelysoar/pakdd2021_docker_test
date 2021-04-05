import requests
from numpy import nan

input1 = {
    'address_log': [['server_47547', 12, 0, 15, 101973, 1016, '2019-06-01 00:00:00', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101975, 1016, '2019-06-01 00:00:00', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101974, 1016, '2019-06-01 00:00:00', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101970, 1016, '2019-06-01 00:00:00', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101971, 1016, '2019-06-01 00:00:00', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101972, 1016, '2019-06-01 00:00:00', 1.0, 1.0]], 'kernel_log': [
        ['2019-06-01 00:00:00', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
         nan, 1.0, nan, nan, nan, nan, nan, 'server_47547', 1, 1.0]],
    'mce_log': [['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:00', 1, 1.0]]}
print("test case 1")
print(requests.post("http://127.0.0.1:8080/tccapi", json=input1).content.decode())

input2 = {
    'address_log': [['server_47547', 12, 0, 15, 100450, 1016, '2019-06-01 00:00:05', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 100451, 1016, '2019-06-01 00:00:05', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 100454, 1016, '2019-06-01 00:00:05', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 100453, 1016, '2019-06-01 00:00:05', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 100455, 1016, '2019-06-01 00:00:05', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 99249, 1016, '2019-06-01 00:00:08', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 100452, 1016, '2019-06-01 00:00:05', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101604, 1016, '2019-06-01 00:00:07', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 99113, 1016, '2019-06-01 00:00:07', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101602, 1016, '2019-06-01 00:00:07', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101605, 1016, '2019-06-01 00:00:07', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101606, 1016, '2019-06-01 00:00:07', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101607, 1016, '2019-06-01 00:00:07', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101701, 1016, '2019-06-01 00:00:41', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101703, 1016, '2019-06-01 00:00:41', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101698, 1016, '2019-06-01 00:00:41', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101700, 1016, '2019-06-01 00:00:41', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36145, 1016, '2019-06-01 00:00:31', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36144, 1016, '2019-06-01 00:00:31', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101603, 1016, '2019-06-01 00:00:07', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 99112, 1016, '2019-06-01 00:00:07', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101699, 1016, '2019-06-01 00:00:41', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36170, 1016, '2019-06-01 00:00:38', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36171, 1016, '2019-06-01 00:00:38', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36174, 1016, '2019-06-01 00:00:38', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36173, 1016, '2019-06-01 00:00:38', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36175, 1016, '2019-06-01 00:00:38', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 98920, 1016, '2019-06-01 00:00:40', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36172, 1016, '2019-06-01 00:00:38', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 98921, 1016, '2019-06-01 00:00:40', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101986, 1016, '2019-06-01 00:00:48', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101991, 1016, '2019-06-01 00:00:48', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101988, 1016, '2019-06-01 00:00:48', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101990, 1016, '2019-06-01 00:00:48', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 101987, 1016, '2019-06-01 00:00:48', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 98988, 1016, '2019-06-01 00:00:56', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 98986, 1016, '2019-06-01 00:00:56', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 98989, 1016, '2019-06-01 00:00:56', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 98990, 1016, '2019-06-01 00:00:56', 1.0, 1.0]], 'kernel_log': nan,
    'mce_log': [['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:05', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:07', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:08', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:08', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:31', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:31', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:31', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:31', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:38', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:40', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:40', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:40', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:41', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:48', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:00:56', 1, 1.0],
                ['server_47547', 'Z', nan, '2019-06-01 00:00:40', 1, 1.0],
                ['server_47547', 'Z', nan, '2019-06-01 00:00:56', 1, 1.0]]}
print("test case 2")
print(requests.post("http://127.0.0.1:8080/tccapi", json=input2).content.decode())

input3 = {
    'address_log': [['server_47547', 12, 0, 15, 99061, 1016, '2019-06-01 00:01:18', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 99062, 1016, '2019-06-01 00:01:18', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 99063, 1016, '2019-06-01 00:01:18', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 99059, 1016, '2019-06-01 00:01:18', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 99060, 1016, '2019-06-01 00:01:18', 1.0, 1.0]], 'kernel_log': [
        ['2019-06-01 00:01:19', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
         nan, 1.0, nan, nan, nan, nan, nan, 'server_47547', 1, 1.0]],
    'mce_log': [['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:01:18', 1, 1.0]]}
print("test case 3")
print(requests.post("http://127.0.0.1:8080/tccapi", json=input3).content.decode())

input4 = {'address_log': [['server_47547', 12, 0, 15, 35906, 1016, '2019-06-01 00:02:36', 1.0, 1.0]],
                          'kernel_log': [
                              ['2019-06-01 00:02:37', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
                               nan, nan, nan, nan, nan, 1.0, nan, nan, nan, nan, nan, 'server_47547', 1, 1.0]],
                          'mce_log': [['server_47547', 'Z', 0.0, '2019-06-01 00:02:36', 1, 1.0],
                                      ['server_47547', 'Z', nan, '2019-06-01 00:02:36', 1, 1.0]]}
print("test case 4")
print(requests.post("http://127.0.0.1:8080/tccapi", json=input4).content.decode())

input5 = {
    'address_log': [['server_47547', 12, 0, 15, 36586, 1016, '2019-06-01 00:03:56', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36587, 1016, '2019-06-01 00:03:56', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36588, 1016, '2019-06-01 00:03:56', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36590, 1016, '2019-06-01 00:03:56', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36591, 1016, '2019-06-01 00:03:56', 1.0, 1.0],
                    ['server_47547', 12, 0, 15, 36589, 1016, '2019-06-01 00:03:56', 1.0, 1.0]], 'kernel_log': nan,
    'mce_log': [['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0],
                ['server_47547', 'Z', 0.0, '2019-06-01 00:03:56', 1, 1.0]]}
print("test case 5")
print(requests.post("http://127.0.0.1:8080/tccapi", json=input5).content.decode())
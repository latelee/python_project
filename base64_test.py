#!/usr/bin/python
# encoding: utf-8
# base64���롢����ʾ��

import base64
# b64encode���ܵ���byte b_string������b_string
passwd = b'rtl8019as=100'

encode_data = base64.b64encode(passwd)
print("base64 encode: %s" % encode_data)

decode_data = base64.b64decode(encode_data)
print("base64 decode: %s" % decode_data)
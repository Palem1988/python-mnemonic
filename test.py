#!/usr/bin/python
#
# Copyright (c) 2013 Pavol Rusnak
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from binascii import hexlify
from random import choice
from mnemonic import Mnemonic

mnemo = Mnemonic()

for i in range(12):
	data = ''.join(chr(choice(range(0,256))) for x in range(8 * (i % 3 + 2)))
	print 'input    : %s (%d bits)' % (hexlify(data), len(data) * 8)
	code = mnemo.encode(data)
	print 'mnemonic : %s (%d words)' % (code, len(code.split(' ')))
	data = mnemo.decode(code)
	print 'output   : %s (%d bits)' % (hexlify(data), len(data) * 8)
	print
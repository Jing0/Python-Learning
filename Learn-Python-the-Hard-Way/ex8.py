# -*- coding:utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
)

sino = "你好，世界！"

print '%s' % sino
print '%r' % sino

string1 = 'Hello World!'
string2 = "Hello World!"

print "%r" % string1
print "%r" % string2
print '%s' % string1
print '%s' % string2

#! /usr/bin/env python

import sys

if len(sys.argv)!=2: 
  print "usage: ./translate.py <language>"
  print "make sure the language exists in the ./language/ folder"
  exit()

lang=sys.argv[1]

try:
  exec("from languages import %s as l")%lang
  langdict=eval("l.%s"%lang)
except ImportError:
  print "Language does not exist"
  print "make sure the language exists in the ./language/ folder"
  exit()

with open("./marked_Grammar","r") as grammar_in:
  with open("./Grammar_%s"%lang, "w+") as grammar_out:
    for line in grammar_in:
      for k,i in langdict.iteritems():
        line=line.replace(k,i)
      grammar_out.write(line)

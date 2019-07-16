#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt

def main(argv):
  SVfile = ''
  outputfile = ''

  try:
    opts, args = getopt.getopt(argv,"hs:o:")
  except getopt.GetoptError:
    print ('transduction_detection.py -s <structual_variants.tsv> -o <outputfile>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('transduction_detection.py -s <structual_variants.tsv> -o <outputfile>')
      sys.exit()
    elif opt in ("-s"):
      SVfile = arg
    elif opt in ("-o"):
      outputfile = arg
  output = open(outputfile, 'w+')
  with open(SVfile) as svs:
    for line in svs:
      if line.startswith("#"):
        continue
      if line.startswith("Chrom"):
        continue
      parts = line.split('\t')
      distance = float(parts[-1][:-1])
      length = parts[3]
      if length != '-' and int(length) < 1000:
        continue
      l1ori = parts[-2]
      if l1ori == '-' and distance > 0 and distance < 1000:
        output.write(line)
      if l1ori == '+' and distance < 0 and distance > -1000:
        output.write(line)

if __name__ == "__main__":
  main(sys.argv[1:])

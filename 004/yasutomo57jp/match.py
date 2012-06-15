#!/usr/bin/env python

import cv2
import numpy
import sys

def drawMatches(img1,img2,keys1,keys2,match):
    img = numpy.hstack((img1,img2)).copy()
    for m in match:
        if m.distance < 0.35: continue
        pt1=map(int,keys1[m.queryIdx].pt)
        pt2=map(int,keys2[m.trainIdx].pt)
        pt2[0]+=img1.shape[0]
        color=map(int,numpy.random.rand(3)*255)
        cv2.line(img, tuple(pt1), tuple(pt2), tuple(color), 1)
    return img

img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])

img1 = cv2.medianBlur(img1,3)
img2 = cv2.medianBlur(img2,3)

surfdetect = cv2.FeatureDetector_create("SURF")
surfextract = cv2.DescriptorExtractor_create("SURF")

keys1=surfdetect.detect(img1)
keys2=surfdetect.detect(img2)

keys1, features1 = surfextract.compute(img1, keys1)
keys2, features2 = surfextract.compute(img2, keys2)

dm = cv2.DescriptorMatcher_create("BruteForce")
match = dm.match(features1,features2)

img=drawMatches(img1,img2,keys1,keys2,match)

cv2.imshow("result", img)
cv2.waitKey()

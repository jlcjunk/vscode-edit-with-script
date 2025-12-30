#!/usr/bin/env bash

# change non-printing character and white spaces to regular spaces
# remove spaces from end of line

sed 's/[^[:print:]]/ /g' | sed 's/\xc2\xa0/ /g' | sed 's/\xEF\xBB\xBF/ /g' | sed 's/ *$//g'
t
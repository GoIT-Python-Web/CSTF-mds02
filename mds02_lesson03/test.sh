#!/bin/bash

echo "Hello world"

#read key
#
#echo "$key"

 function test() {
     local arg="$1"
     echo "Inner function: $arg"
 }

 test "message"

 echo $# $0 $1 $2

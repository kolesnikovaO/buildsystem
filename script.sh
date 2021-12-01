#!/bin/bash
cmake .
cmake --build .
awk -F' ' '{print $3}' vercontrol.h  | sed '1d;2d;3d;4d;5d;$d'

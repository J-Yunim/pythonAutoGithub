#!/bin/bash

function create(){
    cd 
    python create.py $1
    cd /Users/jinyunwang/Documents/Projects/$1
    git init
    git remote add origin https://github.com/J-Yunim/$1.git
    touch README.me
    git add .
    git commit -m"Init"
    git push -u origin master
    code .
}
#!/bin/bash

dirname="task1"
echo $dirname

if [ ! -d "$dirname" ]
then
    echo "Folder doesn't exist. Creating now"
    mkdir ./$dirname
    echo "Folder created"
else
    echo "Folder $dirname exists"
fi

cd ./$dirname

git init

git config --global user.email "gc2708@columbia.edu"
git config --global user.name "GwonJae Cho"

for newfile in {1..5}
do
touch "$newfile"
git add "$newfile"
git commit -m "commit"
done

git branch feature HEAD~4

git checkout feature

for newfile in {6..8}
do
touch "$newfile"
git add "$newfile"
git commit -m "commit"
done

git checkout master

git checkout -b debug

git reset --hard HEAD~2



sha="$(git rev-parse master^)"
echo $sha
sha2="$(git rev-parse master)"
echo $sha2

git branch -D master
git checkout feature

git cherry-pick $sha
git cherry-pick $sha2

git branch master

git reset --hard HEAD~2

git checkout debug

git checkout master -- 7
git add 7
git commit --amend -C HEAD
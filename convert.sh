#!/usr/bin/env bash

for file in ./[0-9][0-9]*.md ; do
  if [ -e "$file" ] ; then
    pandoc "$file" --from gfm -o "$file".pdf -V colorlinks=true -V linkcolor=blue -V urlcolor=blue -V toccolor=gray
    pandoc "$file" --from gfm -o "$file".docx
    pandoc "$file" --from gfm -o "$file".html
    pandoc "$file" --from gfm --standalone -o "$file"-standalone.html
  fi
done

#!/usr/bin/env sh

pandoc -f ipynb+raw_markdown assignments.ipynb -o assignments.md -t gfm

pandoc --mathjax --number-section -f markdown assignments.md -t html | xclip -selection clipboard

pandoc --mathjax --number-sections -f markdown assignments.md -o assignments.html

# other options
# pandoc --number-sections --toc --standalone --mathjax -f markdown assignments.md -o assignments.html

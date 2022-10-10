#/bin/bash

for file in *.pdf
do
  pdfcrop $file $file
done

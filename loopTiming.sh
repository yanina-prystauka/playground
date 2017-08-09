#!/bin/bash
for file in `ls -d *.1D`; do
	name="${file%%.*}" 
	echo "name"
	timing_tool.py \
	-timing "$file" \
	-add_offset -2.5 \
	-write_timing "$name"_adj.1D
done


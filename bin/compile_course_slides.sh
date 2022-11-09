#!/bin/bash

# ----------
# This script compiles the slides .tex files in handout format
# ----------

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]:-${(%):-%x}}" )" >/dev/null 2>&1 && pwd )"
PROJ_ROOT="${THIS_DIR}/.."

if [[ $1 == "--clean" ]]; then
    docker run --rm \
      -v ${PROJ_ROOT}:/workdir \
      -u $(id -u):$(id -g) \
      --workdir /workdir/slides \
    csegarragonz/latex-docker:0.1.2 clean
fi

# Ignore failed searches
shopt -s nullglob

for file_name in ${PROJ_ROOT}/slides/*.tex; do
    base_file_name=$(basename ${file_name})

    # For each file, first check if already have the `handout` tag at the end.
    # Note that this relies on, if `handout` is set, then it must be set at
    # the end (right before {beamer}). This fits the current needs, but if
    # something more generic is needed we can sprinkle more regex magic
    if ! grep -q 'handout]{beamer}' ${file_name}; then
        sed -i 's/]{beamer}/,handout]{beamer}/g' ${file_name}
    fi

    docker run --rm \
      -v ${PROJ_ROOT}:/workdir \
      -u $(id -u):$(id -g) \
      --workdir /workdir/slides \
      csegarragonz/latex-docker:0.1.2 /workdir/slides/${base_file_name} > /dev/null
    if [ $? -eq 0 ]; then
        echo "Processed: ${base_file_name}"
    else
        echo "ERROR! Could not process: ${base_file_name}" >&2
        exit 1
    fi

    # Finally, remove the handout option for the exercises
    if grep -q 'handout]{beamer}' ${file_name}; then
        sed -i 's/,handout]{beamer}/]{beamer}/g' ${file_name}
    fi
done


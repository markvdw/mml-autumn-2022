#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]:-${(%):-%x}}" )" >/dev/null 2>&1 && pwd )"
PROJ_ROOT="${THIS_DIR}/.."

if [[ $1 == "--clean" ]]; then
    docker run --rm \
      -v ${PROJ_ROOT}:/workdir \
      -u $(id -u):$(id -g) \
      --workdir /workdir/exercises \
    csegarragonz/latex-docker:0.1.2 clean
fi

docker run --rm \
  -v ${PROJ_ROOT}:/workdir \
  -u $(id -u):$(id -g) \
  --workdir /workdir/exercises \
  csegarragonz/latex-docker:0.1.2 /workdir/exercises/exercises.tex

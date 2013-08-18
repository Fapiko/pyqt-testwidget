#!/bin/sh

export PYQTDESIGNERPATH=$(pwd)/python
export PYTHONPATH=$PYTHONPATH:$(pwd)/widget

designer-qt4

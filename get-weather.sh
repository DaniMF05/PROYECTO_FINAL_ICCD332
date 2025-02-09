#!/usr/bin/bash
source /home/danielmenendez/miniforge3/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate danielmenendez
python main.py


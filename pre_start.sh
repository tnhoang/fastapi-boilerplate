#! /user/bin/env bash

export PYTHONPATH=$PWD;
poetry shell;
python app/init_data.py;

#!/bin/bash

#python3 -m pytest --capture=no $CASE_FUNC
sleep 5
python3 test_main.py
mv $UPLOADDIR/TEST-*.xml $UPLOADDIR/TEST-ALL.xml
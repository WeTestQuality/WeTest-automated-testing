#!/bin/bash

echo "case start"
python3 demo_cases.py
mv $UPLOADDIR/TEST-*.xml $UPLOADDIR/TEST-ALL.xml
echo "case end"
#!/bin/bash

SCRIPT_FILE="script.zip"
echo "Creating test file"
chmod +x runTest.sh
zip -r "${SCRIPT_FILE}" *py runTest.sh
echo "You should now upload test file '${SCRIPT_FILE}' to WeTest Cloud"
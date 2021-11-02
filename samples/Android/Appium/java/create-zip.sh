#!/bin/bash

SCRIPT_FILE="script.zip"
echo "Creating test file"
zip -r "${SCRIPT_FILE}" src pom.xml runTest.sh
echo "You should now upload test file '${SCRIPT_FILE}' to WeTest Cloud"

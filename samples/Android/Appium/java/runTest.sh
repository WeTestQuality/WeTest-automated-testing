#!/bin/bash
mvn clean test
mv target/surefire-reports/TEST-*.xml $UPLOADDIR/TEST-ALL.xml
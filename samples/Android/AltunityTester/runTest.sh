# AltUnity Tester requires to configure port forwarding from the device to the machine running the tests. 
echo "==> Set AltUnity Tester Port Forwading to 13000 on the device..."
adb forward --remove-all
adb forward tcp:13000 tcp:13000

echo "==> case start..."
python3 demo_cases.py

# In Test Analysis view, You can get all the output files in UPLOADDIR 
mv $UPLOADDIR/TEST-*.xml $UPLOADDIR/TEST-ALL.xml

echo "==> case end..."
# Backend(on raspberry pi)

```
1. Connect the Ultrasonic sensor to the Raspberry Pi correctly.
2. Input 'pip install -- upgrade firebase-admin' in the terminal to install the package
firebase_admin onto the raspberry pi.
3. Connect the Raspberry Pi with the firebase(type: Cloud Firestore) by the given private key.
4. Run the code to check the output distance in the terminal, and you can use the data to adjust
the parameters (namely this part - if average_dis >= 59 or average_dis <= 54)
5. After all parameters are set properly, just run the code. The real-time data will be
automatically updated on the firebase.
```
# Frontend(on Web)

```
1. Input 'cnpm/npm install' in the terminal to install the packages that the codes depend on.
2. Input 'cnpm/npm run serve' in the terminal to run the server.
3. The web page address will be exhibited on the terminal.
```
# Appendix

```
vue/cli 4.5.
python 2.7.
Node.js 14.15.4.
```



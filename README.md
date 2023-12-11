# Appium

## 1. Local Setup
### 1.1. Install Node.js and NPM
```
brew install node
```
### 1.2. Install Appium
```
npm i --location=global appium
```
to check if appium is installed correctly, run:
```appium```
You should see some output that starts with a line like this:
```
[Appium] Welcome to Appium v2.0.0
```
That's it! If you get this kind of output, the Appium server is up and running. Go ahead and quit it (CTRL-C) and move on to the next step, where we'll install a driver for automating Android apps.

### 1.3. Install Android SDK
Download [Android SDK platform tools](https://developer.android.com/tools/releases/platform-tools). You will probably want to download [Android Studio](https://developer.android.com/studio) and manage the SDK tools from within it for the easiest experience.

Set an environment variable pointing to the directory on disk where the Android tools are installed. You can usually find the path to this directory in the Android Studio SDK manager. It will contain the platform-tools and other directories. We need to define and persist the environment variable as ANDROID_HOME.

On Mac, you can do this by adding the following line to your ~/.bash_profile or ~/.bashrc file (and then running source ~/.bash_profile or source ~/.bashrc):
e.g. ~/.zshrc
```
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```
### 1.4. Install JDK
Install the Java JDK (for the most recent Android API levels, JDK 9 is required, otherwise JDK 8 is required). It's easiest to use the OpenJDK packages. Make sure you get the JDK and not the JRE.
```
brew install openjdk
```
Set JAVA_HOME environment variable
e.g. ~/.zshrc
```
export JAVA_HOME=/opt/homebrew/opt/openjdk
```
### 1.5. Validate Setup
Use Android Studio to create and launch an Android Virtual Device (an AVD, otherwise known as an emulator). You may need to download the system images for the API level of the emulator you want to create. Using the AVD creation wizard in Android Studio is generally the easiest way to do all of this.
With the emulator or device connected, you can run ```adb devices``` to verify that your device shows up as connected.

### 1.6. Install Appium Driver
Since the UiAutomator2 driver is maintained by the core Appium team, it has an 'official' driver name that you can use to install it easily via the Appium Extension CLI:
```
appium driver install uiautomator2
```
It should produce output that looks something like:
```
Attempting to find and install driver 'uiautomator2'
✔ Installing 'uiautomator2' using NPM install spec 'appium-uiautomator2-driver'
Driver uiautomator2@2.0.5 successfully installed
- automationName: UiAutomator2
- platformNames: ["Android"]
```


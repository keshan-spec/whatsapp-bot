# Whatsapp chatbot

This is a _basic_ chatbot that uses whatsapp web to chat with a given target
However, it can only respond to messages one by one, Multiple messages MIGHT result in inaccurate replies.

## Drivers

For selenium to be able to open an instance of chrome/firefox or any compatible browser. It needs a Driver, and its default path is `C:\webdriver\`
This can be modified by changing this variable

```
chromepath = r'C:\webdrivers\chromedriver'
```

## Intents.json

```
The intents.json file contains the json data of a set of conversation types with patters and responses for each.
These contents of the patterns and responses can be modifed as wanted. 
```

## New words

Any new words or phrases not available in the json data will be added to the new words.txt in the following format:

```
Bro-Fri Jul 12 19:48:15 2019: bye
[TARGET]-[DATE] [TIME] : [MESSAGE]
```

```
NOTE : if anything doesn't load or open. Please check:
1. The chromedriver path
2. The xpath values with your whatsapp web styles
3. The target name
4. Scan the QR Code within 25 seconds ( can be changed in the init method)
```

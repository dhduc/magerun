#MAGERUN
Helper for Magento 2
## Feature
- Optimize task for execute magento 2 console command <br>


## For Window
###Install **python 2.7** <br>
Get install file from [python.org](https://www.python.org/download/releases/2.7/)

###Set **PATH** environment
Go to Control Panel > All Control Panel Items > System > Advanced System Settings <br>
In the System Properties Window, Click Environment Variables > Edit **PATH** from **User variables** and add path below at the end of value string (separate by ';')
```
C\Python27
```
###Setup <br>
Copy **magerun.py** from **window\terminal** folder to python folder (**C\Python2.7**) <br>
Using file correct with your terminal (**gitbash** or **cmder**) <br>

###Usage <br>
Just type **magerun.py** in the root folder of magento 2 project on your terminal
```
magerun.py
``` 
## For Ubuntu/Linux
Make sure that python installed on your OS <br>
###Setup <br> 
Copy **magerun.py** file to **/usr/bin/** folder <br>
You can use it without file extension such as **/usr/bin/magerun** alternative **/usr/bin/magerun.py** because the system understands it's a python shell scripting.
```
sudo cp magerun.py /usr/bin/magerun.py
```
Grant executable permission
```
sudo chmod u+x /usr/bin/magerun.py
```

###Usage <br>
Just type **magerun.py** (or **magerun**) in the root folder of magento 2 project on your terminal
```
magerun.py
```

##Custom
You can change its name depend on your mind 

##Screenshot
Main Menu <br>
![](screenshot/magerun.png?raw=true)

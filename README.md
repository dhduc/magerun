#MAGERUN
Helper for Magento 2
## For Window
1. Install **python 2.7** <br>
Get install file from [python.org](https://www.python.org/download/releases/2.7/)

2. Set **PATH** enviroment
```
PATH:=...;C\Python2.7
```

3. Setup <br>
Copy **magerun.py** from **window\terminal** folder to python folder (**C\Python2.7**)
Using file correct with your terminal (**gitbash** or **cmder**)

4. Usage <br>
Just type **magerun.py** in the root folder of magento 2 project on the your terminal
```
magerun.py
``` 
## For Ubuntu/Linux
Make sure that python installed on your OS <br>
1. Setup <br> 
Copy **magerun.py** file to **/usr/bin/** folder <br>
You can use it without file extension such as **/usr/bin/magerun** alternative **/usr/bin/magerun.py** because the system understand it's a python shell scripting.
```
sudo cp magerun.py /usr/bin/magerun.py
```
Grant executable permission
```
sudo chmod u+x /usr/bin/magerun.py
```

2. Usage <br>
Just type **magerun.py** (or **magerun**) in the root folder of magento 2 project on the your terminal
```
magerun.py
```

##Custom
You can change its name depend on your mind 

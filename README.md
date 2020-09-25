# Automated Python Script Execution
This demonstrates how to configure a Windows system to execute a certain task (here: run an python script) automatically.

## 1.Step: Write python code
in our small example, the code we'd like to execute is stored in ``script.py``.

## 2. Step write caller script
By default, the Windows system executes `*.bat` files. 
We therefore write a .bat script  `caller_script.bat` which executes the above python file.

## 3. Step Schedule an OS-Event
We first run the 'Aufgabenplanung' app.
![](Images/step1.PNG) 


Then, create a new simple event.

![](Images/step2.PNG) 


Use the assistent to navigate through the setup. Give a name

![](Images/step3.PNG)

set an interval

![](Images/step4.PNG) 

and start day.

![](Images/step5.PNG) 

Define what to do

![](Images/step6.PNG) 

and plug in the path to the caller script from above.

![](Images/step7.PNG) 

You finally get a review field. You get check the checkbox to see more settings.

![](Images/step8.PNG) 

here you can define more triggers in cae you'd like to run the scipt multiple times a day: 
Use the 'new' button to add more.

You can also edit the current event and set a repitition rate. Therefore click on 'bearbeiten'  

![](Images/step9.PNG)

and set further repetitions. 

![](Images/step10.PNG) 

## 4. Step: You're done
Happy scripting :)


# Disclaimer
IPA 2020 for internal uses

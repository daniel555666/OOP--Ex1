# OOP--Ex1 <br />
## Elevator system design algorithm
By Dvir Gev and Daniel Zaken
OOP Ex1 exercise ariel university. In this task we are required to execute an algorithm, to find the best time for the total calls in offline mode.<br />
In this algorithm we use an idea from the last task that was of the online algorithm, by that we implemented cmd and simulates the time and reception of the calls to know which elevator to assign to which call.
<br />
## Functions at the algorithm
**candidateElevators** - Return the best elevator fot the call.<br />
**calculateTime** - The function get two floor numbers and will calculate how much time take the elevator to go from one to the other.<br /> 
**allocateAnElevator** - The function get call and allocate the best elevator for her.<br />
**cmd** - Get the current time and move all the elevators.<br />
**algorithm** - Simulates the time of the scenario and calls the functions cmd and allocateAnElevator.<br />
**runTester** - activate the tester.<br />
<br />
## Class
class Elevatorsv<br />
class Building<br />
class CallForElevator<br />
<br />

## Link,UML,Results
link to instructions of Ex1 https://docs.google.com/document/d/1D4aW2vRaKjwtSBY1gDyCC6SNRE5TRGwMerGIXUMkI_Y/edit
<br />
## for run the code: python Ex1.py input\Ex1_Buildings\B2.json input\Ex1_Calls\Calls_a.csv myOutput.csv 

![image](https://user-images.githubusercontent.com/92304153/142245777-f47dff89-a507-4ba9-b2a1-7244c50688b5.png)
![image](https://user-images.githubusercontent.com/92304153/142393305-edc221eb-0a51-4acd-b56e-3b674e5aa093.png)

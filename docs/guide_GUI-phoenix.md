# GUI for Climate Services Information Systems

## Example: Phoenix

* Birdhouse provides a web-based application where scientific data assessment can be executed over a Graphical User Interphase (GUI), the provided package is [Phoenix](https://github.com/bird-house/pyramid-phoenix). Phoenix is a web application to work with processing services, which can be made accessible via an online portal. Here is an example demonstrator developed within the [CLINT Project](https://climateintelligence.eu/) providing services for extreme weather event detection. The services are deployed on virtual machines at the German Climate Computing Center [DKRZ](https://www.dkrz.de/en/). In the following example we run the infill missing values process over a portal based on the [Phoenix App](https://github.com/bird-house/pyramid-phoenix).

## Infill with Duck

Go to the Phoenix app:
https://clint.dkrz.de

* Choose the *Duck* processing service
![](images/phoenix-duck-wps.png)

* Use the *ClintAI* process
![](images/phoenix-duck-processes.png)

* Select a HadCRUT5 dataset for the infill process
![](images/phoenix-duck-infill.png)

* Wait for the process to finish ...
![](images/phoenix-duck-monitor.png)

* When the process has finished go to the *details* to show the outputs
![](images/phoenix-duck-outputs.png)

* Outputs: a plot before the infill
![](images/duck-plot-before.png)

* Outputs: a plot after the infill
![](images/duck-plot-after.png)
# ELLevator ReadMe
#### _Potential Engineer Interview Submission_

##### Summary
This project simulates the behavior of a single elevator.

##### Languages and Libraries Used
- Python 3.7
- tkinter (GUI Library for Python)

##### Files Included
- main.py
- ellevator.py
- manage_queue.py
- accept_input.py
- readme.md

### How to Run
- Be sure you have installed Python 3.7 or higher and all files listed above are in the same directory
- In a Terminal shell, navigate to the directory chosen in the above step
- Type the command: 
```sh
python3 main.py
```
- You will see text output in your terminal and a popup window prompting you for input. Select any floor buttons you'd like add to the Elevator's queue. When you are finished providing input, press Submit.
- The Elevator will continue producing output until it arrives at its next open door destination. At this time, you will be prompted again to provide input. To provide no input, simply press Submit.
- _Alternatively, you can run this from an environment of your choice. You will still run main.py to inititate the program_

### Assumptions, Limitations, and Decisions Made
##### Assumptions
- When finished with its list of requests, the Elevator should return to the first floor (or lobby)
- There is only one Elevator
- There is only one master queue, which exists outside of and is accessed by the Elevator
- The Elevator accepts an input of (floor, direction) from the 'outside'. This summons the Elevator.
- The Elevator accepts an input of (floor, exit) from the 'inside'. This is logged as a destination.

##### Decisions
- The Elevator moves incremenetally up and down along a list of integers between and including a provided minimum and maximum floor number. At each floor, the Elevator will decide if it should change direction and decide if it should stop.
- The Elevator **will stop** at a floor if there exists an external summon request for the current floor _in the **same** direction the Elevator is already traveling_
- The Elevator **will stop** at a floor if there exists an internal request for the current floor, _regardless of direction_
- The Elevator **will not stop** at a floor if there exists an external summon request for the current floor _in the **opposite** direction the Elevator is already traveling_

##### Limitations (personal and technical)
- The Elevator can only accept input while the doors are open. I think the user interface is not really the point of this exercise, but I did try to make one. It bounces around a bit, as it is a pop-up window.
- The Elevator's behavior is hard-coded at the moment. It cannot quickly become another flavor of Elevator.
- The Elevator currently checks direction and it checks if it should open its doors _twice_ in main.py. This allows the Elevator to turn around at the top or bottom of its path. I imagine there is a more efficient way to ensure the Elevator turns around, but I left it this way for my and your (mostly my) sanity.
"""
AcceptInput object is an interface that interacts with a passed Queue() object
AcceptInput allows for both internal and external input
- Click floor buttons to add instructions to Queue()
- Click Undo to remove most recent instruction
- Click Submit to add all instructions to the queue and terminate current window
"""

from tkinter import *
import tkinter
from manage_queue import Queue

class AcceptInput(tkinter.Tk):
    def __init__(self, floor, direction, min_floor, max_floor, queue):
        super().__init__()

        #new_summons_list holds values from any buttons pressed until Submit is pressed and window exits
        self.new_summons_list = []

        #define functions for all buttons
        def append(d):
            self.new_summons_list.append(d)
            summon_list_display.insert(END, d)

        def submit(q):
            for summon in self.new_summons_list:
                summon = summon.split()
                q._add_to_queue(int(summon[0]), summon[1])
            close()

        def undo():
            self.new_summons_list.pop()
            summon_list_display.delete(END)

        def close():
            self.destroy()

        """
        Create first paned window to display 
        floor, direction, destination list, and selections
        """
        w1 = PanedWindow(orient=VERTICAL)
        w1.pack()

        pane_1_items = [
            tkinter.Label(text="ELLevator", font='Helvetica 18 bold'),
            tkinter.Label(text="Current Floor: " + str(floor)),
            tkinter.Label(text="Current Direction: " + str(direction).upper()),
            tkinter.Label(text="Current Destinations: " + ', '.join([str(x) for x in queue._get_queue().keys()])),
            tkinter.Label(text="Selected Inputs", font='Helvetica 14 bold')
        ]

        for item in pane_1_items:
            w1.add(item)

        summon_list_display = tkinter.Listbox()
        w1.add(summon_list_display)

        """
        Create second paned window to display and populate input from 
        OUTSIDE the Elevator i.e. summon Elevator with up/down and floor info
        """
        w2 = PanedWindow(w1, orient=VERTICAL)
        w1.add(w2)

        w2.add(tkinter.Label(text="Summon From Outside Elevator", font='Helvetica 16 bold'))
        w2.add(tkinter.Button(w1, text=str(min_floor) + " Up", command=lambda j='1 Up': append(j)))

        #add all external input buttons except for min/max floors. assign them the function 'append' to
        # append a new input to new_summons_list on click
        i = min_floor + 1
        while i < max_floor:
            c = str(i) + " Up"
            w2.add(tkinter.Button(w1, text=str(i) + " Up", command=lambda j=c: append(j)))
            k = str(i) + " Down"
            w2.add(tkinter.Button(w1, text=str(i) + " Down", command=lambda j=k: append(j)))
            i += 1

        w2.add(tkinter.Button(w2, text=str(max_floor) + " Down", command=lambda j=str(max_floor) + ' Down': append(j)))
        w2.add(tkinter.Label(text="Select Destination from Inside Elevator", font='Helvetica 16 bold'))

        """
        Create third paned window to display and populate input from 
        INSIDE the Elevator i.e. just number destinations
        """
        w3 = PanedWindow(w2, orient=HORIZONTAL)
        w2.add(w3)

        w3.add(tkinter.Button(w3, text=str(min_floor), command=lambda j=str(min_floor) + ' Exit': append(j)))

        #add all internal input buttons except for min/max floors. assign them the function 'append' to
        # append a new input to new_summons_list on click
        i = min_floor+1
        while i < max_floor:
            c = str(i) + " Exit"
            w3.add(tkinter.Button(w3, text=str(i), command=lambda j=c: append(j)))
            i += 1

        w3.add(tkinter.Button(w3, text=str(max_floor), command=lambda j=str(max_floor) + ' Exit': append(j)))

        """
        Append Submit Bottom to second pane so it appears at the bottom of the interface...
        Probably a better way to do this
        """
        w2.add(Button(w2, text="Undo", command=undo))
        w2.add(Button(w2, text="Submit Input", command=lambda j=queue: submit(j)))

        mainloop()

if __name__ == "__main__":
  app = AcceptInput(floor=3, direction='up', min_floor=1, max_floor=10, queue=Queue())
  app.mainloop()
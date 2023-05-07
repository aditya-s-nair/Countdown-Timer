                           # # # Name: Aditya S Nair # # #
import tkinter as tk
import datetime

class Timer(tk.Frame):
    def __init__(self,master):
        super().__init__(master)  ##Background of the widget
        self.create_widgets()     ##Creation of the widget
        self.master=master
        master.title("Countdown Timer")
        self.show_widgets()
        self.seconds_left=0
        self.timer_on = False
   
    def show_widgets(self):
        self.label.pack()    #Labeling
        self.entry.pack()    #textbox
        self.start.pack()    #Start button
        self.pause.pack()    #Pause button
        self.stop.pack()     #Stop  button
        self.reset.pack()    #Re-enter button
        
        
        
    def create_widgets(self):
        self.label=tk.Label(self,text="Enter the time in seconds")
        self.entry=tk.Entry(self,justify="center")
        self.entry.focus_set() 
        self.reset=tk.Button(text="Re-enter",
                             command=self.reset_button)
        self.stop=tk.Button(text="Reset/Stop",
                             command=self.stop_button)
        self.start=tk.Button(text="Start",
                             command=self.start_button)
        self.pause = tk.Button(text="Pause/Resume",
                             command=self.pause_button)
        
    # <<coundown portion>>    
    def countdown(self):
        self.label["text"]=self.convert_seconds_left_to_time()
        if self.seconds_left:
            self.seconds_left-=1
            self._timer_on=self.after(1000,self.countdown)
            if self.seconds_left==0:
                self.label.config(text="Done!")
        else:
            self._timer_on=False
        
        
    def start_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.pause.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.pause.pack()
        self.stop.pack()
        self.reset.pack()
        print("<<< The timer has been started >>>\n")

    def pause_button(self):
            print("<<",self.seconds_left,"second/s left>>\n")
            print("<<<The timer has now resumed>>>\n")

        
    def reset_button(self):
        self.seconds_left=0
        self.stop_timer()
        self._timer_on=False
        self.label["text"]="<< Enter the time in seconds:: >>"
        self.start.forget()
        self.pause.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.pause.pack()
        self.stop.pack()
        self.reset.pack()
        print("<<< Please re-enter the time required >>>\n")
        
    
    def stop_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
        print("<<< The timer has now been reset >>>\n")
        
            
    def stop_timer(self):
        if self.timer_on:
            self.after_cancel(self.timer_on)
            self.timer_on=False
        
        
    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)

#main loop of the code
if __name__=="__main__":
    root=tk.Tk()
    root.resizable()
    root.geometry("500x300")            
    countdown=Timer(root)
    countdown.pack()
    root.mainloop()
    
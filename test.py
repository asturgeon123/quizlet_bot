import tkinter as tk
from answer_scrapper import find_answer


root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    query=name_var.get()
    print("Question : " + query)   


    name_var.set("")
    Output.delete('1.0', tk.END)
    Output.insert(tk.END, find_answer(query)[1])  


name_label = tk.Label(root, text = 'Question', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

Output = tk.Text(root, height = 5,
              width = 50,
              bg = "light cyan")


# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=1,column=1)
name_entry.grid(row=2,column=1)
sub_btn.grid(row=4,column=1)
Output.grid(row=5,column=1)



  
# performing an infinite loop
# for the window to display
root.mainloop()
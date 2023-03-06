from tkinter import * 
from Bookings import *

# class Table(object): pass
# var_dict = Table()

#Setup
window = Tk()
window.title('Restaurant Manager')
window.geometry('900x620')


# bookings = open("Bookings.txt", 'r').readlines()
bookings_object = Bookings("Bookings.txt")




#--------------------------------------------------------------------------------------





def display_availability(time):

    available = bookings_object.check_availability(str(time))
    error_message.config(fg="#303030")
    error = False 

    try:
        if len(time) != 5:
            error = True
            print('length')
        if time[2] != ":" and time[2] != '.':
            error = True
            print("middle")
        if time[0].isdigit() == False or time[1].isdigit() == False:
            error = True 
            print('isdigit')
        if time[3].isdigit() == False or time[4].isdigit() == False:
            error = True 

        if error == True:
            error_message.config(fg="red")
            return 
    except:
        error_message.config(fg="red")
        return


    new_counter = 0
    for tab in dictionary:
        new_counter += 1
        dictionary[tab].config(bg='red', fg='#303030')

        if 'table_' + str(new_counter) in available:
            dictionary[tab].config(bg='green', fg="#303030")
 




#--------------------------------------------------------------------------------------





def Make_Booking(requested_time):
    
    free_tables = bookings_object.check_availability(str(requested_time))

    try:
        file = open("Bookings.txt", 'a')
        file.write(f"{name_entry.get()} @ {requested_time} on {free_tables[0]}\n") 
        booking_confirmation.config(fg='green')
        booking_confirmation.grid(row=7, column=2)
        window.after(2500, lambda: booking_confirmation.config(fg='#303030'))
        booking_confirmation.grid(row=7, column=2)
        file.close()
    except:
        booking_confirmation.config(text=' No Availability ', fg='red')
        booking_confirmation.grid(row=7, column=2)
        window.after(2500, lambda: booking_confirmation.config(fg='#303030'))
        booking_confirmation.grid(row=7, column=2)





#--------------------------------------------------------------------------------------





#Tables in a grid 

table_1 = Label()
table_2 = Label()
table_3 = Label()
table_4 = Label()
table_5 = Label()
table_6 = Label()
table_7 = Label()
table_8 = Label()
table_9 = Label()

dictionary = {
    table_1 : Label(text='Table 1', fg='Black', padx=40, pady=20, bg='Light Grey'),
    table_2 : Label(text='Table 2', fg='Black', padx=40, pady=20, bg='Light Grey'),
    table_3 : Label(text='Table 3', fg='Black', padx=40, pady=20, bg='Light Grey'),
    table_4 : Label(text='Table 4', fg='Black', padx=40, pady=20, bg='Light Grey'),
    table_5 : Label(text='Table 5', fg='Black', padx=40, pady=20, bg='Light Grey'),
    table_6 : Label(text='Table 6', fg='Black', padx=40, pady=20, bg='Light Grey'),
    table_7 : Label(text='Table 7', fg='Black', padx=40, pady=20, bg='Light Grey'),
    table_8 : Label(text='Table 8', fg='Black', padx=40, pady=20, bg='Light Grey'),
    table_9 : Label(text='Table 9', fg='Black', padx=40, pady=20, bg='Light Grey')

}




#Empty Label to Create Left Border 
border = Label(text="     " ,padx = 40 ,pady = 20)

#Title 
title = Label(text=" Tom's Diner ", padx=100, pady=20)

#Bookings 

bookings_title = Label(text=' Create a Booking ', pady = 20)
name_label= Label(text=' Name ')
name_entry = Entry( relief='raised')
time_label = Label(text=' Time ')
time_entry = Entry(relief='raised')
make_booking = Button(text=' Make Booking ', pady=10, command= lambda : Make_Booking(time_entry.get()))
booking_confirmation = Label(text=' Booking Confirmed', padx=20, pady= 5, fg='#303030')

#Check Availability

check_avail_title = Label(text=' Check Availability ')
time_label2 = Label(text=' Time ')
time_entry2 = Entry(relief='raised')
check_avail = Button(text=' Check Availability ', command = lambda : display_availability(time_entry2.get()), pady=10)
error_message = Label(text='Error', padx=20, pady= 5, fg='#303030')




#-----------------------------------------------------------------------------------------------------------




#Placing Everything on the Screen

dictionary[table_1].grid(row=1, column=1, padx=5, pady=5)
dictionary[table_2].grid(row=1, column=2, padx=5, pady=5)
dictionary[table_3].grid(row=1, column=3, padx=5, pady=5)
dictionary[table_4].grid(row=2, column=1, padx=5, pady=5)
dictionary[table_5].grid(row=2, column=2, padx=5, pady=5)
dictionary[table_6].grid(row=2, column=3, padx=5, pady=5)
dictionary[table_7].grid(row=3, column=1, padx=5, pady=5)
dictionary[table_8].grid(row=3, column=2, padx=5, pady=5)
dictionary[table_9].grid(row=3, column=3, padx=5, pady=5)


border.grid(row=1, column=0, padx=5, pady=5)
title.grid(row= 0, column = 2, padx=5,pady=5)


bookings_title.grid(row=4, column=1)
name_label.grid(row=5, column=1)
name_entry.grid(row=6, column=1)
time_label.grid(row=7, column=1)
time_entry.grid(row=8, column=1)
make_booking.grid(row=9, column=1)


booking_confirmation.grid(row=7, column=2)
error_message.grid(row=8, column=2)


check_avail_title.grid(row=4, column=3)
time_label2.grid(row=5, column=3)
time_entry2.grid(row=6, column=3)
check_avail.grid(row=7, column=3)


window.mainloop()


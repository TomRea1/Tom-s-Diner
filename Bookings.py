
class Bookings():

    def __init__(self, bookings):
        self.bookings = bookings

    
    def get_tables(self):

        lines = open(self.bookings, "r").readlines()

        table_list = ''

        for booking in lines:
            table_list = table_list + booking[-2]  

        return table_list

    def get_times(self):

        lines = open(self.bookings, "r").readlines()

        times = ''
        for booking in lines:
            letter_counter = 0
            on_time = False 
            for letter in booking:
                letter_counter += 1
                if letter == 'o' and booking[letter_counter] == 'n':
                    break
                if on_time == True:
                    times += letter
                if letter == "@":
                    on_time = True

        return times.split()

    def get_bookings(self):

        tables_dict = {
                1 : [],
                2 : [],
                3 : [],
                4 : [],
                5 : [],
                6 : [],
                7 : [],
                8 : [],
                9 : []
            }
        
        # Create availability dictionary 
        counter = -1
        for table in self.get_tables():
            counter += 1
            tables_dict[int(table)].append(self.get_times()[counter])

        return tables_dict
    
    def check_availability(self, time_req):

        available_tables = []
        counter = 0


        for tab in self.get_bookings():
            counter += 1
            
            if str(time_req) not in self.get_bookings()[tab]:
                available_tables.append("table_" + str(counter))
                
        return available_tables

# with open('Bookings.txt') as bookings_file:

#     bookings = bookings_file.readlines()  

# x = Bookings(bookings)

# print(x.check_availability('20.00'))

        
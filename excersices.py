
# # 1. Library Book Tracker
# bootcamps = {}

# def add_book():
    
#     author = input('Enter the name of the author: ')
#     title = input('Enter the title of the book: ')
#     users = int(input('Enter how many users has the book: '))
#     while users <0:
#         users = input('you must type a positive number: ')
#         break
    
#     bootcamps['Name'] = author
#     bootcamps['title'] = title
#     bootcamps['users'] = users
    
# def find_book():
    
#     search = input('Enter the title of the book: ')
#     if search == bootcamps['title']:
#         print('The book is avaliable')
#     while search != bootcamps['title']:
#         search = input('Try again, enter the name of the book: ')
#         break
    
# def show_books():
#     print('This is your current library', bootcamps)

# add_book()
# find_book()
# show_books()


# # 2. Student Grade Manager
# students = {}
# grade_l = []

# def add_student():
#     student = input('Enter the name of the student: ')
#     students['Student name: '] = student
    
# def add_grade():
 
#     number_grades = int(input('Enter how many grades you want to type: '))
#     while number_grades <0:
#         number_grades = int(input('Enter a positive number: '))
#         break
#     for i in range(number_grades):
#         grades = int(input('Enter the grade: '))
#         grade_l.append(grades)
        
#     students['Grades'] = grade_l

# def get_average(): 
#     for o in grade_l:
#         summation = sum(grade_l)
#         average = summation / len(grade_l)
        
#         students['Average'] = average

# add_student()
# add_grade()
# get_average()

        
# 3. Restaurant Menu Editor
# inventory = {}

# def add_dish():
#     name = input('Enter the name of the dish: ')
#     price = float(input('Enter the price of the dish: '))
#     availability = input('Enter the availability of the dish(A or U): ')
    
#     inventory['Name'] = name
#     inventory['Price'] = price
#     inventory['Availability'] = availability
    
# def change_availability():
#     modifier = input('Enter the name of the dish to modify availability: ')
#     if modifier == inventory['Name']:
#         change = input('Enter the new value(A or U): ')
#         inventory['Availability'] = change
#     else:
#         print('Wrong name typed, try again')
    
# def total_available_price():
#     print('Theese are the dishes that are Available: ', inventory['Name'],':',inventory['Availability'])
    
# add_dish()
# change_availability()
# total_available_price()


# 4. Warehouse Box Counter
# warehouse = {}
# def add_box():
#     print('Enter the kind of box between: small,medium and big\n')
#     kind_box = input('enter the size of the box: ')
#     print('\nNow enter the amount of boxes')
#     amount = int(input('Enter the amount of boxes: '))
#     while amount < 0:
#         amount = int(input('Please enter a positive number: '))
    
#     warehouse['Size'] = kind_box
#     warehouse['Amount'] = amount
    
# def update_quantity():
#     updater = input('Enter the size of the box: ')
#     if updater == warehouse['Size']:
#         updater = int(input('Enter the new amount: '))
#     else:
#         print('Invalid size')
        
#     warehouse['Amount'] = updater
    
# def has_enough():
#     choice = input('enter the size of the box you are looking for(small,medium,big): ')
#     while choice != warehouse['Size']:
#         choice = input('Please enter a valid size: ')
#         break
#     user_a = int(input('Enter the amount of boxes you would like: '))
#     if user_a <= warehouse['Amount']:
#         print('boxes bought succefully')
#     elif user_a > warehouse['Amount']:
#         print('Not enough boxes to buy :( )')

# add_box()
# update_quantity()
# has_enough()
        

# # 5. Movie Rating System

# movies = {}
# rates = []
# def add_movie():
#     movie = input('Type the name of the movie: ')
#     movies['Title of the movie'] = movie
    
# def rate_movie(): 
#     name = input('Enter the name of the movie to rate: ')
#     while name != movies['Title of the movie']:
#         name = input('Enter a valid name: ')
#         continue
    
#     if name == movies['Title of the movie']:
#         rate = int(input('Enter a number between 1-5 to rate the movie: '))
#         while rate <=0 or rate >5:
#             rate = int(input('Enter a number between the range: '))
#             continue
        
#         rates.append(rate)
    
# def average_rating():
#     for i in rates:
#         summation = sum(rates)
#         result = summation / len(rates)
        
#         movies['Average rating'] = result
        
# add_movie()
# rate_movie()
# average_rating()

# # 6. Online Course Tracker
# bootcamps = {}

# def add_course():
#     title = input('Enter the title of the course: ')
#     duration = int(input('Enter the duration of the course in months: '))
#     while duration <= 0:
#         duration = int(input('You must type a positive number: '))
#         continue

#     users = int(input('Enter how many users are in the course: '))
#     while users <= 0:
#         users = int(input('You must type a positive number: '))
#         continue

#     bootcamps['Title'] = title
#     bootcamps['Duration'] = duration
#     bootcamps['Users'] = users

# def update_enrollment():
#     course = input('Enter the name of the course: ')
#     while course != bootcamps['Title']:
#         course = input('Enter a valid name of a course: ')
#         continue

#     if course == bootcamps['Title']:
#         update = int(input('Enter a number to update the users of the course: '))
#         while update <= 0:
#             update = int(input('Enter a positive number: '))

#         bootcamps['Users'] = update

# def filter_by_hours():
#     if 'Duration' in bootcamps and bootcamps['Duration'] > 5:
#         print(f"Course '{bootcamps['Title']}' has a duration above 5 hours: {bootcamps['Duration']} months")
#     else:
#         print(f"Course '{bootcamps['Title'] if 'Title' in bootcamps else ''}' does not exceed 5 hours duration.")

# add_course()
# update_enrollment()
# filter_by_hours()

# # 7. To-Do List Organizer

# to_do = {}

# def add_task():

#     task = input('Enter the name of the task: \n')
#     description = input('Enter the description of the task: \n')
#     priority = input('Enter the priority of the task (high, medium, low): \n')
#     while priority not in ['high', 'medium', 'low']:
#         priority = input('Please enter a valid priority (high, medium, low): ')
#         continue

#     to_do['Task'] = task
#     to_do['Description'] = description
#     to_do['Priority'] = priority

# def complete_task():
#     task = input('Enter the name of the task to mark as complete: \n')
#     if task == to_do['Task']:
#         print('Task completed')
#     else:
#         print('Task not found')

# def filter_tasks():
#     priority = input('Enter the priority to filter by (high, medium, low): \n')
#     if priority == to_do['Priority']:
#         print('Task found:', to_do['Task'], 'the state of the task is: ', to_do['Priority'])
#     else:
#         print('No tasks found with that priority')

# add_task()
# complete_task()
# filter_tasks()


# # 8. Digital Wallet
# wallet = {}

# def add_expense():
#     category = input('Enter the expense category: ')
#     amount = float(input('Enter the expense amount: '))
#     if category in wallet:
#         wallet[category] += amount
#     else:
#         wallet[category] = amount

# def total_spent():
#     total = sum(wallet.values())
#     print(f'Total money spent: {total}')

# def expense_percentages():
#     if not wallet:
#         print("No expenses recorded.")
#         return
#     total = sum(wallet.values())
#     category = input('Enter the category to see its percentage: ')
#     if category in wallet:
#         percent = (wallet[category] / total) * 100
#         print(f'Percentage spent on {category}: {percent:.2f}%')
#     else:
#         print('Category not found.')

# add_expense()
# add_expense()
# total_spent()
# expense_percentages()

# # 9. Pet Adoption Center
# pets = []

# def add_pet():
#     name = input('Enter the name of the pet: ')
#     species = input('Enter the species of the pet: ')
#     age = int(input('Enter the age of the pet: '))
#     while age <= 0:
#         age = int(input('Please enter a positive age: '))
#     pets.append({'name': name, 'species': species, 'age': age})

# def find_by_species():
#     search_species = input('Enter the species to search for: ')
#     found = [pet for pet in pets if pet['species'].lower() == search_species.lower()]
#     if found:
#         for pet in found:
#             print(f"Name: {pet['name']}, Age: {pet['age']}")
#     else:
#         print('No pets found for that species.')

# def older_than():
#     min_age = int(input('Enter the minimum age to filter by: '))
#     while min_age < 0:
#         min_age = int(input('Please enter a non-negative minimum age: '))
#     found = [pet for pet in pets if pet['age'] > min_age]
#     if found:
#         for pet in found:
#             print(f"Name: {pet['name']}, Species: {pet['species']}, Age: {pet['age']}")
#     else:
#         print('No pets found older than that age.')

# add_pet()
# add_pet()
# find_by_species()
# older_than()


# # 10. Gym Membership System
# members = []

# def register_member():
#     name = input('Enter member name: ')
#     plan = input('Choose plan (basic/premium): ').lower()
#     while plan not in ['basic', 'premium']:
#         plan = input('Invalid plan. Choose "basic" or "premium": ').lower()
#     # Validate price is positive (though fixed here)
#     price = 20 if plan == 'basic' else 50
#     while price <= 0:
#         print('Price must be positive.')
#         price = int(input('Enter a positive price: '))
#     paid = input('Has the member paid? (yes/no): ').lower() == 'yes'
#     members.append({'name': name, 'plan': plan, 'price': price, 'paid': paid})

# def change_plan():
#     name = input('Enter member name to change plan: ')
#     for member in members:
#         if member['name'].lower() == name.lower():
#             new_plan = input('Enter new plan (basic/premium): ').lower()
#             while new_plan not in ['basic', 'premium']:
#                 new_plan = input('Invalid plan. Choose "basic" or "premium": ').lower()
#             member['plan'] = new_plan
#             member['price'] = 20 if new_plan == 'basic' else 50
#             while member['price'] <= 0:
#                 print('Price must be positive.')
#                 member['price'] = int(input('Enter a positive price: '))
#             print(f"{name}'s plan updated to {new_plan}.")
#             return
#     print('Member not found.')

# def unpaid_members():
#     print('Unpaid members:')
#     found = False
#     for member in members:
#         if not member['paid']:
#             print(f"Name: {member['name']}, Plan: {member['plan']}, Price: {member['price']}")
#             found = True
#     if not found:
#         print('All members have paid.')

# register_member()
# register_member()
# change_plan()
# unpaid_members()


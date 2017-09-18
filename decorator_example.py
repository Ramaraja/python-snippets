# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.

# Adds a welcome message to the string
def messageWithWelcome(str):

	# Nested function
	def addWelcome():
		return "Welcome to "

	# Return concatenation of addWelcome()
	# and str.
	return addWelcome() + str

# To get site name to which welcome is added
def site(site_name):
	return site_name

print messageWithWelcome(site("Python training"))



# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
def decorate_message(fun):
 
    # Nested function
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)
 
    # Decorator returns a function
    return addWelcome
 
@decorate_message
def site(site_name):
    return site_name;


print site("Clash of clans!!")

def attach_data(func):
       func.data = 3
       return func
 
@attach_data
def add (x, y):
       return x + y


print add(5,10)
print add.data

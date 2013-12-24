Python
======
Hi ,

Here I have attached the respective program for below ten exercises.

Why Python. There are many high-level languages. The language you will be learning is
Python. Python is one of the easiest languages to learn and use, while at the same time being very powerful:
It is used by many of the most highly productive professional programmers. A few of the places that use
Python extensively are Google, the New York Stock Exchange, Industrial Light and Magic, .... Also Python
is a free language! If you have your own computer, you can download it from the Internet.

 Writing Your First Python Program

    Create a folder called PythonPrograms on your C:\ drive. You will be storing all your Python programs in this folder.
    Go to Start and either type Run in the Start Search box at the bootom or click on Run.
    Type in notepad in the field called Open.
    In Notepad type in the following program exactly as written: 


# File: Ex1.py

print "Hello World!"

    Go to File and click on Save as.
    In the field Save in browse for the C: drive and then select the folder PythonPrograms.
    For the field File name remove everything that is there and type in ex1.py.
    In the field Save as type select All Files
    Click on Save. You have just created your first Python program. 

Running Your First Program

    Go to Start and click on Run.
    Type cmd in the Open field and click OK.
    A dark window will appear. Type cd C:\ and hit the key Enter.
    If you type dir you will get a listing of all folders in your C: drive. You should see the folder PythonPrograms that you created.
    Type cd PythonPrograms and hit Enter. It should take you to the PythonPrograms folder.
    Type dir and you should see the file ex1.py.
    To run the program, type python Ex1.py and hit Enter.
    You should see the line Hello World!
    Congratulations, you have run your first Python program. 

 Exercise 1: A Good First Program
  print "Hello World!"
  print "Hello Again"
  print "I like typing this."
  print "This is fun."
  print 'Yay! Printing.'
  print "I'd much rather you 'not'."
  print 'I "said" do not touch this.'
  
  The above program only print "Hello world".


 Exercise 2: Comments And Pound Characters 
 
 # A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print "I could have code like this." # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print "This will run."


  
 Exercise 3: Numbers And Math
    + plus
    - minus
    / slash
    * asterisk
    % percent
    < less-than
    > greater-than
    <= less-than-equal
    >= greater-than-equal

Exercise 4: Variables And Names
 program:
 
 cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
 
The above programe is explain the variables and names.
 
 Variable :
You can use any letter, the special characters "_" and every number provided
you do not start with it. 

White spaces and signs with special meanings in Python, as "+" and "-" are
not allowed. 

I usually use lowercase with words separated by underscores as necessary to
improve readability.

Remember that variable names are case sensitive. 

 
 Exercise 5: More Variables And Printing
 ex5.py:
 
 my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)

This program is explain the embed variables inside a string by using specialized format sequences and then putting the variables at the end with a special syntax that tells Python, "Hey, this is a format string, put these variables in there."
 
 Exercise 6: Strings And Text
 ex6.py
 x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
 
 A string is usually a bit of text you want to display to someone, or "export" out of the program you are writing. Python knows you want something to be a string when you put either " (double-quotes) or ' (single-quotes) around the text. You saw this many times with your use of print when you put the text you want to go to the string inside " or ' after the print. Then Python prints it.

Strings may contain the format characters you have discovered so far. You simply put the formatted variables in the string, and then a % (percent) character, followed by the variable. The only catch is that if you want multiple formats in your string to print multiple variables, you need to put them inside ( ) (parenthesis) separated by , (commas). It's as if you were telling me to buy you a list of items from the store and you said, "I want milk, eggs, bread, and soup." Only as a programmer we say, "(milk, eggs, bread, soup)."
 
 Exercise 7: More Printing
 ex7.py
 print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


The above program output is like this
$ python ex7.py
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese Burger
 
 
 Exercise 8: Printing, Printing
 ex8.py
 formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
 
 
Your output is like that
 $ python ex8.py
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'

 
 
 Exercise 9: Printing, Printing, Printing
 
 ex9.py
 # Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

Your output like this
$ python ex9.py
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug

There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
 
 Exercise 10: What Was That?
 ex10.py
 tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


Your output:
Look for the tab characters that you made. In this exercise the spacing is important to get right.

$ python ex10.py
   I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
   * Cat food
   * Fishies
  * Catnip
  * Grass
The above program is just print the characters.
 


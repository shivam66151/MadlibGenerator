import tkinter
from tkinter import *

root = Tk()
root.geometry("300x300")
root.title('MAD LIB GENERATOR')

Label(root, text = 'Mad Libs Generator \n have Fun!', font='arial 20 bold').pack()
Label(root, text = 'Click Any One:', font='arial 15 bold').place(x=40, y=80)

def madlib1():

    animals= input('Enter a animal name:')
    profession= input('Enter a profession:')
    cloth= input('Enter a cloth name:')
    name= input('Enter a name:')
    things= input('Enter a thing:')
    place= input('Enter a place name:')
    verb= input('Enter a verb:')
    food= input('Enter a food:')

    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +
    ' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + 
    ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + 
    ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

def madlib2():

    adjective= input('Enter a adjective:')
    color= input('Enter a color:')
    person= input('Enter a person name:')
    adjective1= input('Enter a adjective:')
    thing= input('Enter a thing:')
    place= input('Enter a place name:')
    insect= input('ENter a insect name:')
    food= input('Enter a fod:')
    verb= input('Enter a verb')

    print('Last night I dreamed I was a ' +adjective+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjective1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')
    
def madlib3():

    person = input('enter person name: ')
    color = input('enter color: ')
    foods = input('enter food name: ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')
   
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')

Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()





# doms stuff
import os
import sys
import time
import datetime
import pytz
localtime = datetime.datetime.now(pytz.timezone('US/Eastern'))
#agenda
#1. add log file for every school
#2. add folders for every school!!!
print(localtime,"EST")

      
while True:
  localtime = datetime.datetime.now(pytz.timezone('US/Eastern'))
  schools = open("schools.txt").readlines()
  
  global schoolname
  #why global
  schoolname = input("What is the name of the school?: ").lower()
  #why lower case
  #easy to search
  if schoolname + "\n" in schools:
    print("School already exists\nwould you like to view this school?")
    while True:
      schoolview = input("[y/n]?: ")
      if schoolview == "y":
        #print(f"You are now viewing {schoolname}")
        log = open("schools/"+schoolname+"/"+schoolname+"-log.txt","a")
        log0002 = str(f"School {schoolname} has been accessed at {localtime} EST;")
        log.write(log0002)
        log.write("\n")
        log.close()
        break
      elif schoolview == "n":
        print("ok exiting school menu...")
        sys.exit() 
        # 
    break       
        
            

  else: 
    #directory
    os.mkdir("schools/"+schoolname)
    #new school
    schools1 = open("schools.txt","a")
    #append
    schools1.write(schoolname)
    schools1.write("\n")
    schools1.close()   
    school = open("schools/"+schoolname+"/"+schoolname+".txt","x")
    school.close()
    teachers = open("schools/"+schoolname+"/"+schoolname+"-teachers.txt","x")
    teachers.close()
    students = open("schools/"+schoolname+"/"+schoolname+"-students.txt","x")
    students.close()
    log = open("schools/"+schoolname+"/"+schoolname+"-log.txt","a")
    log0001 = str(f"School {schoolname} has was created at {localtime} EST;")
    log.write(log0001)
    log.write("\n")
    log.close()
    print("\n...School Generated...\n")
    break


    



class School():
  #print some kind of nice greeting statement/bar
  def display_title_bar():
      # Clears the terminal screen, and displays a title bar.
      os.system('clear')
                
      print("\t**********************************************")
      print(f"\t   ***    Welcome to {schoolname.title()}  ***")
      print("\t**********************************************")
  def get_user_choice():
      # Let users know what they can do.
      print("\n[1] See a list of members")
      print("[2] Add a Member")
      print("[3] School Population")
      print("[4] Population of teacher body.")
      print("[5] Population of student body.")
      print("[6] View Log")
      print("[q] Quit.")
      
      return input("What would you like to do? ")
      
  def show_names():
      # Shows the names of everyone who is already in the list.
      print("\nSchool employees and students.\n")
      for name in populationCount:
          print(name.title())
  def show_log():
      # Shows the names of everyone who is already in the list.
      print("\nSchool log\n")
      for line in log123:
          print(line.title())        
          
  def get_new_name():
      # Asks the user for a new name, and stores the name if we don't already
      #  know about this person.
      new_name = input("\nPerson's Name: ").lower()
      if new_name + "\n" in schoolname:
          print(f"\n%s is already in the {schoolname} database." % new_name.title())
      else:
          file = open("schools/"+schoolname+"/"+schoolname+".txt","a")
          file.write(new_name)
          file.write("\n")
          file.close()
          while True:
            profession = input(f"Is {new_name} a student or a teacher?: ")
            if profession == "teacher":
              teach = open("schools/"+schoolname+"/"+schoolname+"-teachers.txt","a")
              teach.write(new_name)
              teach.write("\n")
              teach.close()
              log = open("schools/"+schoolname+"/"+schoolname+"-log.txt","a")
              log0003 = str(f"Teacher ({new_name}) has been added to the system at: {localtime} EST;")
              log.write(log0003)
              log.write("\n")
              log.close()
              break
            elif profession == "student":
              student = open("schools/"+schoolname+"/"+schoolname+"-students.txt","a")
              student.write(new_name)
              student.write("\n")
              student.close()
              log = open("schools/"+schoolname+"/"+schoolname+"-log.txt","a")
              log0004 = str(f"Student ({new_name}) has been added to the system at: {localtime} EST;")
              log.write(log0004)
              log.write("\n")
              log.close()
              break  
            else:
              print("\nInvalid Answer\nPlease use [student] or [teacher].\n")  
          print(f"\nWelcome %s! to {schoolname}.\n" % new_name.title())

  ### MAIN PROGRAM ###

  # Set up a loop where users can choose what they'd like to do.


  choice = ''
  display_title_bar()
  while choice != 'q':    
      #names = open("people.txt").readlines()
      localtime = datetime.datetime.now(pytz.timezone('US/Eastern'))
      global populationCount
      populationCount = open("schools/"+schoolname+"/"+schoolname+".txt").readlines()
      global log123
      log123 = open("schools/"+schoolname+"/"+schoolname+"-log.txt").readlines()
      teacherCount = open("schools/"+schoolname+"/"+schoolname+"-teachers.txt").readlines()
      studentCount = open("schools/"+schoolname+"/"+schoolname+"-students.txt").readlines()
      choice = get_user_choice()
      
      # Respond to the user's choice.
      display_title_bar()
      if choice == '1':
          show_names()
      elif choice == '2':
          get_new_name()
      elif choice == '3':
          print("Members: ",len(populationCount))
      elif choice == '4':
          print("Teachers: ",len(teacherCount))
      elif choice == '5':
          print("Students: ",len(studentCount),)
      elif choice == '6':
          show_log()               
      elif choice == 'q':
          print("\nThanks for your visit and support. Bye.")
      else:
          print("\nI didn't understand that choice.\n")
          #time.sleep(5)
          #display_title_bar()


School()












#Step1: Get user input
#Step2: Check if user input is in people.txt
#Step3: If yes, print "Welcome back to school you little demon"
#Step4: If no, append to the file and print "Welcome to hell new kid."
#Step5: Should we have a menu?
#If so Option1: see the list, Option2: Add a name, Option3 quit
#Thumbsup from Dom: file handling
#Thumbsup from Cedar: 
#it looks nice, 1] See a list of students.[2] Tell me about someone new. [q] Quit.
#How do I make this into a class?
#Do I need more than one py files?


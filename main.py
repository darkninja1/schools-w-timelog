# doms school machine with log
#  #works#isgood#tryit
import os
import sys
import time
import datetime
import pytz
localtime = datetime.datetime.now(pytz.timezone('US/Eastern'))

print(localtime,"EST")

      
while True:
  localtime = datetime.datetime.now(pytz.timezone('US/Eastern'))
  schools = open("schools.txt").readlines()
  global password
  password = open("password.txt").readlines()
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
        while True:
          pass2 = input("Enter School Administrator password - ")
          if (pass2+"\n" in password):
            user1 = schools.index(schoolname+"\n")
            global pass1
            pass1 = password.index(pass2+"\n")
            if (user1 == pass1):
              log = open("schools/"+schoolname+"/"+schoolname+"-log.txt","a")
              log0002 = str(f"School {schoolname} has been accessed at {localtime} EST;")
              log.write(log0002)
              log.write("\n")
              log.close()
              break
            else:
              print("\nInvalid Password\n")
              sys.exit()  
          else:
            print("\nInvalid Password\n")
            sys.exit("Invalid Password")     
        break
      elif schoolview == "n":
        print("ok exiting school menu...")
        sys.exit() 
        # 
    break       
        
            

  else: 
    #directory
    os.mkdir("schools/"+schoolname)
    password123 = input("Please add an administartor password - ")
    pass123 = open("password.txt","a")
    pass123.write(password123)
    pass123.write("\n")
    pass123.close()
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
      print("[7] Administrator")
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
  def settings():
    #settings (not yet operational)
    while True:
      # Clears the terminal screen, and displays a title bar.
      os.system('clear')
                
      print("\t**********************************************")
      print(f"\t   ***    Welcome to {schoolname.title()} Administrator! ***")
      print("\t**********************************************")
      print("\nWelcome to settings\n")
      print("\n[1] Delete Student")
      print("[2] Delete Teacher")
      print("[3] Change Admin Password")
      print("[q] Quit.")
      admin_input = input("Admin ~ ")
      if admin_input == "1":
        admin_student = input("What student would you like to delete?: ").lower()
        if (admin_student+"\n" in studentCount):
          delst2 = populationCount.index(admin_student+"\n")
          del populationCount[delst2]
          delst = studentCount.index(admin_student+"\n")
          del studentCount[delst]
          newscount = open("schools/"+schoolname+"/"+schoolname+"-students.txt","w")
          for line in studentCount:
            newscount.write(line)
          newscount.close()
          newpcount = open("schools/"+schoolname+"/"+schoolname+".txt","w")
          for line in populationCount:
            newpcount.write(line)
          newpcount.close()
          log = open("schools/"+schoolname+"/"+schoolname+"-log.txt","a")
          log0005 = str(f"Student ({admin_student}) has been removed from the system at: {localtime} EST;")
          log.write(log0005)
          log.write("\n")
          log.close()
          print(log0005)
        else:
          print(f"\nStudent {admin_student} does not exist.\n")
      elif admin_input == "2":
        admin_teacher = input("What teacher would you like to delete?: ").lower()
        if (admin_teacher+"\n" in teacherCount):
          delst2 = populationCount.index(admin_teacher+"\n")
          del populationCount[delst2]
          delst = teacherCount.index(admin_teacher+"\n")
          del teacherCount[delst]
          newscount = open("schools/"+schoolname+"/"+schoolname+"-teachers.txt","w")
          for line in teacherCount:
            newscount.write(line)
          newscount.close()
          newpcount = open("schools/"+schoolname+"/"+schoolname+".txt","w")
          for line in populationCount:
            newpcount.write(line)
          newpcount.close()
          log = open("schools/"+schoolname+"/"+schoolname+"-log.txt","a")
          log0006 = str(f"Teacher ({admin_teacher}) has been removed from the system at: {localtime} EST;")
          log.write(log0006)
          log.write("\n")
          log.close()
          print(log0006)
        else:
          print(f"\nTeacher {admin_teacher} does not exist.\n")   
      elif admin_input == "3":
        current_pass = input("Please enter the current password - ")
        if (current_pass+"\n" == password[pass1]):
          new_pass = input("Please enter the new password - ")
          password[pass1] = (new_pass+"\n")
          password3 = open("password.txt","w")
          for line in password:
            password3.write(line)
          password3.close()
          print("\nNew Password has been set.\n")
          log = open("schools/"+schoolname+"/"+schoolname+"-log.txt","a")
          log0007 = str(f"New system password has been set by admin at: {localtime} EST;")
          log.write(log0007)
          log.write("\n")
          log.close()
        else:
          print("Invalid Password")  
      elif admin_input == "q":
        break     
      else:
        print("\nInvalid Input\n")      

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
      global teacherCount
      teacherCount = open("schools/"+schoolname+"/"+schoolname+"-teachers.txt").readlines()
      global studentCount
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
      elif choice == '7':
          administrator = input("Admin Passcode - ")
          if (administrator+"\n" == password[pass1]):
            settings()
          else:
            print("\nInvalid Password\n")
      elif choice == 'q':
          print("\nThanks for your visit and support. Bye.")
      else:
          print("\nI didn't understand that choice.\n")
          


School()













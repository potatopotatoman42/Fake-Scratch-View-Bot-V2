from scratchclient import ScratchSession
import random, time
numbers = ["1","2","3","4","5","6","7","8","9","0"]
valid = False
projects = []
last_project = 0
counter = 0
session = ScratchSession("potatopotatopotato48","passwordpassword")
project = session.get_project(815058096)
#print(project.get_comments(all=True))
c_project = session.get_project(815058096)
users = []







while 1 == 1:
    print("Length of comments list is {0}".format(project.get_comments(all=True)))
    print("Current projects list: {0}".format(projects))
    if len(project.get_comments(all=True)) == 0:
        print("we be viewing projects boiiiiiiii")
        for f in range(-1,len(projects)-1):
            c_project = session.get_project(int(projects[f]))
            c_user = users[f]
            try:
                if c_project.author.username == c_user and not c_user == "potatopotatopotato48":
                    c_project.post_comment("Really, trying to use a view bot? Tsk tsk, this project and your comment have both been reported.")
                    c_project.report("9","Trying to use a view bot on their project. I also reported their comment.")

                projects.pop(f)
                
                if not f == 0:
                    f -= 1

            #print(c_project.view_count)
            except:
                print("Pre list: {0}. Deleted project {1} from list. Post list: {2}.f is {3}".format(projects,projects.pop(),projects,f))
                f -= 1
                print("f is {0}".format(f))

    else:
        counter = 0
        
        for e in  range(0,len(project.get_comments(all=True)),1):
            print("e is {}".format(e))
            print("length of comments list: {}".format(len(project.get_comments(all=True))))
            #print("last project is {}".format(last_project))
            print("list: {}".format(projects))
            if e > len(project.get_comments(all=True)):
                continue
            else:
                comment = project.get_comments(all=True)[e-1]
          
            valid = True
            print("Current comment is ({0})".format(comment.content))
            for i in range(0,len(comment.content)):
                print("i cycle, i is {0} and comment is {1}".format(i,comment.content))
                if not comment.content[i] in numbers or comment.content in projects:
                    valid = False
                    print("Comment ({}) is invalid.".format(comment.content))

                    comment.delete()
                    e -= 1
                    break
      
            if valid:
                projects.append(comment.content)
                print("Added project ({}) to list.".format(comment.content))
                users.append(comment.author)
                comment.report()
                comment.delete()
                e -= 1
            project.set_description(projects)
        #last_project = counter




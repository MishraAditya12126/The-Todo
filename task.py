import sys
import time
def  help():
    message="""Usage :-
$ .\\task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ .\\task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ .\\task del INDEX            # Delete the incomplete item with the given index
$ .\\task done INDEX           # Mark the incomplete item with the given index as complete
$ .\\task help                 # Show usage
$ .\\task report               # Statistics"""
    sys.stdout.buffer.write(message.encode("utf8"))

def add(s,n):
    fh=open("task.txt","a")
    fh.write(s+f" [{n}]"+"\n")
    fh.close()
    print(f"Added task: \"{s}\" with priority {n}")

def ls():
    f=open("task.txt")
    print(f.read())
all_commands=globals()
all_commands["ls"]()
# if __name__=="__main__":
#     args=sys.argv
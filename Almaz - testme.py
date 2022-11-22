
# The congratulations method needs to check periodically if any changes were made, if so display it
# Every time the user changes the button to grey, the amount of credits in that button should be added to the overall credit
# and displyed to the UI_MainWindow
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print("Doing stuff...")
    # do your stuff
    sc.enter(5, 1, do_something, (sc,))

s.enter(5, 1, do_something, (s,))
s.run()

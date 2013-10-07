import praw
import time

def nameChecker():
	USER_AGENT="User name catcher by /u/badpokerface12 for /u/PM_ME_YOUR_TITS"  #describes what the bot does 
	USER_NAME='' # your username for logging in and checking 
	PASS_WD='' # put your password here
	
	reddit=praw.Reddit(USER_AGENT) #Creats bot
	reddit.login(USER_NAME,PASS_WD)
	print reddit.is_logged_in()
	
	checked=set()
	while True:
		print "Getting Comments"
		all_comments=reddit.get_comments('test',limit=2000)
		#flatten=praw.helpers.flatten_tree(all_comments)
		for comments in all_comments:
			print comments.id
			if (comments.body==USER_NAME or comments.body=='/u/PM_ME_YOUR_TITS_GIRL') and comments.id not in checked:
				print "Name mentioned in " + comments.id
				reddit.send_message(USER_NAME,"Username Mentioned",captcha=None)
				checked.add(comments.id)
		print "getting ready to sleep"
		time.sleep(30)
	
def main():
    print "getting ready to start looking for your user name"
    nameChecker()

main()

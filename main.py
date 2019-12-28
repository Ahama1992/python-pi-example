
def main(message):

// This was the conflict, pretty neat ey!
<<< HEAD
    // This comment however is from pi dir
    // Let's see what conflict  arises
=======
    // This is to print a message
    // This file is from pi2 dir on my local machine
>>> refs/remotes/origin/master
    print(message)


main("Hello beautiful")

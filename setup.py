# Local system variables and setup
import platform


theirGitDirectory = 'root/TheirGit'
myGitDirectory = '/root/MyGit'


def determineEnvironment():
    hostOS = platform.system()
    if hostOS == "Mac":
        vmWareType = "fusion"
    else:
        vmWareType = "ws"

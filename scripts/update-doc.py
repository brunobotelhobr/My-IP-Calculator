import argparse  # type: ignore
import os  # type: ignore

print("----------------------------------------------------------------")
print("Updating Documentation, point github sites to the correct branch")
print("----------------------------------------------------------------")

# Get the tirst argument
parser = argparse.ArgumentParser()
parser.add_argument("branch", help="The doucmentation branch")
args = parser.parse_args()

DOC_BRANCH = args.branch

# Run a command and get the output as a string

CURRENT_BRANCH = os.popen("git rev-parse --abbrev-ref HEAD").read()
print("Current Branch: " + CURRENT_BRANCH)
print("Documentation Branch: " + DOC_BRANCH)

os.system("git checkout " + DOC_BRANCH + " > /dev/null")
print("Current Branch: " + DOC_BRANCH)

os.system("git add * > /dev/null")
os.system("git commit -m 'Task: Update Documentation' > /dev/null")
os.system("git push --set-upstream origin " + DOC_BRANCH)
os.system("git checkout " + CURRENT_BRANCH + "  > /dev/null")

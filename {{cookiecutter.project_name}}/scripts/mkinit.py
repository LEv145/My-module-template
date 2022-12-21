import subprocess
import shlex
from sys import argv


subprocess.run(shlex.split(f"mkinit {argv[1]} -w --black --nomods --relative --recursive"))

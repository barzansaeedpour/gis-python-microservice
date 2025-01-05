
import subprocess

INPUT_FOLDER = "./input/"
OUTPUT_FOLDER = "./output"

TEIGHA_PATH = "/opt/ODAFileConverter/ODAFileConverter.exe"
OUTVER = "ACAD2018"
OUTFORMAT = "DXF"
RECURSIVE = "0"
AUDIT = "1"
INPUTFILTER = "*.DWG"

# Command to run
cmd = ["wine", TEIGHA_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]

# Run the command
subprocess.run(cmd)

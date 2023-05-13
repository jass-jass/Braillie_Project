import subprocess
import os

folder_path = '/media/usb'
des_path = '/home/sanjana/Braillie_Project/input_files'

def copy_files(source_path, destination_path):
        #command to copy files
        COPY_COMMAND = ['cp',source_path,destination_path]
        #execute the command
        try:
           subprocess.check_call(COPY_COMMAND)
        except subprocess.CalledProcessError as e:
                print("Error:",e)


def check_folder():
        if(os.path.exists('/home/sanjana/Braillie_Project/input_files')):
                pass
        else:
                os.mkdir('/home/sanjana/Braillie_Project/input_files')
                print('Folder created')

#command to find the files with .txt extension
FILES_COMMAND = ['find',folder_path,'-type','f','-name','*.txt']

#list to store the files found
output = subprocess.run(FILES_COMMAND, capture_output=True , text=True)

#storing the file paths in a available
file_paths = output.stdout.splitlines()


if(len(file_paths)==0):
        print("No pdf or text files found")
else:
        #print the file paths
        for path in file_paths:
                file = path.split('/')     #converting string into a list to pr$
                print("Press 1 to copy the folder")
                print(file[3:])
                var = input()
                if(var == '1'):
                        check_folder()
                        copy_files(path,des_path)
                else:
                        print("No file to copy")

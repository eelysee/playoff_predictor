import os
import subprocess

'''
To use these scrits: 
Copy imports to .py file
Copy wanted function into a .py file.

Call function at the end of file
Replace file_location full directory path

run .py scrupt by calling in terminal with 'python script_file_name'

Then delete utility file
'''


def tar_peek(file_location):
    '''
    this function takes a look inside all .tar.xz files in a directory and prints what is in them.
    to run copy it into a .py file and call the file in the same directory you want to check 
    import os
    import subprocess
    '''
    for filename in os.listdir(file_location):
        if filename.endswith('.tar.xz'):
            full_path = os.path.join(file_location,filename)
            result = subprocess.run(['tar', '-tf', full_path], capture_output=True, text=True)

            print(f'Contents of {filename}:\n')
            print(result.stdout)
            print('='*40)


file_location = '.'
tar_peek(file_location)

def tar_unpack(file_location):
    '''
    End tar_peek()
    this code unpacks all tarball/zipped filess in place
    to run copy it into a .py file and call the file in the same directory you want to check 
    import os
    import subprocess
    '''
    for filename in os.listdir(file_location):
        if filename.endswith('.tar.xz'):
            full_path = os.path.join(file_location,filename)
            result = subprocess.run(['tar', '-xf', full_path])


file_location = '.'
tar_unpak(file_location)

def delete_tar(file_location):
    '''
    End tar_ unpak()
    this code deletes all tarball/zipped filess in place
    to run copy it into a .py file and call the file in the same directory you want to check 
    import os
    '''
    for filename in os.listdir(file_location):
        if filename.endswith('.tar.xz'):
            full_path = os.path.join(file_location,filename)
            os.remove(full_path)

file_location = '.'
delete_tar(file_location)
# End delete_tar()

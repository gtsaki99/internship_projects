import os
import subprocess
import time

r_path = r'location_of_automator_file\Automator_temp' #location of temporary file, up to personal choice
f1_path = r'location_of_daily_activity_script\Daily_activity.py' #location of Daily_activity.py script
f2_path = r'location_of_compilation_to_website_script\Compilation_to_website.py' #location of Compilation_to_website.py script
p_path = r'location_of_python_executable\python.exe' #location of python executable

def to_do():
    if os.path.exists(r_path + '1' + '.txt'):
        os.remove(r_path + '1' + '.txt')
    if os.path.exists(r_path + '2' + '.txt'):
        os.remove(r_path + '2' + '.txt')
    f = open(r_path + "1" +'.txt', 'w+')
    f.write(r'"' + p_path + r'" "' + f1_path + r'"')
    f.close()
    f_name, ext = os.path.splitext(r_path + '1' + '.txt')
    os.rename(r_path + '1' + '.txt', f_name + ".bat")
    subprocess.call([r_path + '1' + '.bat'])
    os.remove(r_path + '1' + '.bat')
    f_n = open(r_path + '2' + '.txt', 'w+')
    f_n.write(r'"' + p_path + r'" "' + f2_path + r'"')
    f_n.close()
    f_name, ext = os.path.splitext(r_path + '2' + '.txt')
    os.rename(r_path + '2' + '.txt', f_name + ".bat")
    subprocess.call([r_path + '2' + '.bat'])
    os.remove(r_path + '2' + '.bat')

if to be run continuously apply this instead of to_do()
while True:
    to_do()
    time.sleep(86400)
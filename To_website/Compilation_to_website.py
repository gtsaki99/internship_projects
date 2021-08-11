import pandas as pd
import os
from ftplib import FTP

#Will need pip istall pandas in command line before run from command line

#paths needed
start_path = r'location_of_start\start.txt' #location of the text file with the specs of the html
s_path = r'source_path\custom_file_name.' #location of the daily activity file
r_path= r'location_we_want\custom_file_name.' #location of the resulting html file completely up to personal choice 
#create the html file
names_list = [None] * 44
for i in range(44):
    names_list[i] = str(i + 1)
df = pd.read_csv(s_path + 'csv', names = names_list)
if os.path.exists(r_path + 'html'):
    os.remove(r_path + 'html')
start_f = open(start_path, "r")
start = start_f.read()
start_f.close()
res = open(r_path + 'txt', "w+")
res.write(start)
res.write("\n  <tr>")
res.write("\n   <th> </th>")
for i in range(44):
    res.write("\n   <th>" + names_list[i] + "</th>")
res.write("\n  <tr>")
for i in range(len(df.index)):
    res.write("\n  </tr>")
    res.write("\n   <td>" + str(i + 1) +"</td>")
    for j in range(44):
        str_c = str(df.loc[i, str(j + 1)])
        if str_c == "nan":
            str_c = " "
        res.write("\n   <td>" + str_c + "   </td>")
    res.write("\n  </tr>")
del df
res.write("</table>\n" + "\n</body>\n" +"</html>")
res.close()
f_name, ext = os.path.splitext(r_path + 'txt')
os.rename(r_path + 'txt', f_name + ".html")
#upload to server
#server details
host = "__"		#ftp server details:hostname, username and password
username = "__"
password = "__"
#connect and upload
ftp = FTP(host=host)
login_status = ftp.login(user=username, passwd=password)
ftp.cwd('/htdocs')
fp = open(r_path + 'html', 'rb')
ftp.storbinary('STOR %s' % os.path.basename(r_path + 'html'), fp, 1024)
fp.close()
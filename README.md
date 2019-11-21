# Remove Control(Unwanted) chars from the files

## Background

TL;DR - Atleast one time  in your programming life, you may come across this kind of task, "Removing the controlling chars from the file"

A File with control chars.

```bash
mymachine$ cat -v 2018-04-16_01-29-42_rx5755_uSxfjOL58SXrmPGfkw43LdHaOFBm0f7uDSLzQuIapl.data\
Script started on Mon 16 Apr 2018 01:29:42 AM EDT\
To run a command as administrator (user "root"), use "sudo <command>".^M\
See "man sudo_root" for details.^M\
^M\
[2018-04-16 01:29:43][rx5755@webubuntu ~] $~ ls -ltrh^M\
total 32K^M\
-rw-r--r-- 1 rx5755 rx5755 8.8K Mar 30 18:11 examples.desktop^M\
-rw-rw-r-- 1 rx5755 rx5755   73 Apr 15 20:16 helloworld.c^M\
-rwxrwxr-x 1 rx5755 rx5755 8.5K Apr 15 20:16 ^[[0m^[[01;32mhelloworld^[[0m^M\
-rw-rw-r-- 1 rx5755 rx5755   10 Apr 15 22:40 delete.file^M\
[2018-04-16 01:29:44][rx5755@webubuntu ~] $~ exit^M
```
to a file without control chars
```bash
mymac_machine$ cat 2018-04-16_01-29-42_rx5755_uSxfjOL58SXrmPGfkw43LdHaOFBm0f7uDSLzQuIapl.data\
Script started on Mon 16 Apr 2018 01:29:42 AM EDT\
To run a command as administrator (user "root"), use "sudo <command>".\
See "man sudo_root" for details.\
\
[2018-04-16 01:29:43][rx5755@webubuntu ~] $~ ls -ltrh\
total 32K\
-rw-r--r-- 1 rx5755 rx5755 8.8K Mar 30 18:11 examples.desktop\
-rw-rw-r-- 1 rx5755 rx5755   73 Apr 15 20:16 helloworld.c\
-rwxrwxr-x 1 rx5755 rx5755 8.5K Apr 15 20:16 helloworld\
-rw-rw-r-- 1 rx5755 rx5755   10 Apr 15 22:40 delete.file
```
## How to run

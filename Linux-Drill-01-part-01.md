#
# Linux Drill 01
#

1. Create a new dir within / tmp dir. [ mkdir /tmp/dir1 ]
2. Change its owner to root and back to kali user. [ chown root /tmp/dir1 @---> chown kali /tmp/dir1 ]
3. Create a new username student1. [ useradd student1 ]
4. Add this user to sudo group. [ usermod -aG sudo student1 ]
5. Create a new file called sudo.txt within the dir you created on step 1. [ touch /tmp/dir1/sudo.txt @---> usermod -aG sudo student2 ]
6. Create a new user named 'student2' and add it to the sudo group. [ useradd student1  @---> usermod -aG sudo student2 ]
7. Find ' sudo ' group users and write (copy) them to the file from step 5. [ grep '^sudo:' /etc/group | cut -d: -f4 | tr ',' '\n' > /tmp/dir1/sudo.txt ] 
8. Start from the root ( / ) dir and find a file named "rockyou.txt" on the file system using find command. [ find / -name "rockyou.txt" 2>/dev/null ]
9. Copy the file you found to the dir you created on step 1. [ sudo cp /path/to/the-file/rockyou.txt /tmp/dir1/ ]  ---> we can combine the last 2 steps into one command by --> [ sudo find / -name "rockyou.txt" 2>/dev/null | xargs -I '{}' cp '{}' /tmp/dir1/ ]
10. Modify the permissions to make it readable and writable only, by you only. [ chown root:root /tmp/dir1/rockyou.txt && chmod 600 /tmp/dir1/rockyou.txt ]
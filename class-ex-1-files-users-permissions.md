#
# Files, Users & Permissions - Linux Fundamentals
#

Class Exercise –1

#
1. Use the `touch` command in your terminal to create five empty text files with the following names; file1.txt, file2.txt, fileA.txt, fileA1.txt, fileB2.txt (use one line command to perform this step).
2. Use a single line command to list only files with the name “file” in them.
3. Use a single line command to list only files with the name “file” followed by a number.
4. Use a single line command to list only files ending with a letter and a number before the extension (e.g., thisF4.txt)
5. Use a single line command to remove files with the name “file” followed by a capital letter.

#
┌──(root㉿kali)-[~/Documents]
└─# touch file1.txt file2.txt fileA.txt fileA1.txt fileB2.txt                                 
                                                                                                                    
┌──(root㉿kali)-[~/Documents]
└─# ls *file*          
file1.txt  file2.txt  fileA1.txt  fileA.txt  fileB2.txt
                                                                                                                    
┌──(root㉿kali)-[~/Documents]
└─# ls *file[0-9]*
file1.txt  file2.txt
                                                                                                                    
┌──(root㉿kali)-[~/Documents]
└─# ls *file[a-zA-Z][0-9]*
fileA1.txt  fileB2.txt
                                                                                                                    
┌──(root㉿kali)-[~/Documents]
└─# ls *file[A-Z]*        
fileA1.txt  fileA.txt  fileB2.txt

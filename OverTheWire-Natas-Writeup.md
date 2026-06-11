OverTheWire Natas Writeup

Platform: OverTheWire
Category: Web Security
Date: June 2026

Level 0 → 1

Goal: Find the password for the next level

Work:

Viewed page source
Found password hidden inside an HTML comment

What I Learned:

HTML comments are visible to everyone
Hidden source code is not security
Level 1 → 2

Goal: Find the next password

Work:

Right-click was disabled
Used View Source / Developer Tools
Located the password in page source

What I Learned:

Client-side restrictions can always be bypassed
Browser controls are not security controls
Level 2 → 3

Goal: Find the next password

Work:

Inspected page source
Found reference to /files/
Visited the directory directly
Located file containing the password

What I Learned:

Directory listing can expose sensitive files
Source code often reveals hidden resources
Level 3 → 4

Goal: Find the next password

Work:

Checked /robots.txt
Found hidden directory /s3cr3t/
Browsed to the directory
Retrieved password

What I Learned:

robots.txt is public
Hidden paths are not protected paths
Level 4 → 5

Goal: Access the protected page

Work:

Observed Referer-based access control
Modified HTTP Referer header
Reloaded request
Received password

What I Learned:

HTTP headers are client-controlled
Referer should never be trusted for authorization
Level 5 → 6

Goal: Become logged in

Work:

Inspected browser cookies
Found loggedin=0
Changed value to loggedin=1
Refreshed page

What I Learned:

Cookies can be modified by users
Authorization must be enforced server-side
Level 6 → 7

Goal: Discover the secret value

Work:

Viewed application source code
Found included file secret.inc
Accessed file directly
Retrieved secret and submitted it

What I Learned:

Source code review is powerful
Included files may leak sensitive information
Level 7 → 8

Goal: Find the next password

Work:

Observed page parameter usage
Tested file inclusion behavior
Accessed sensitive local file
Retrieved next password

Vulnerability: Local File Inclusion (LFI)

What I Learned:

User-controlled file paths are dangerous
LFI can expose credentials and source code
Level 8 → 9

Goal: Recover the secret

Work:

Reviewed source code
Identified multiple encoding transformations
Reversed each step
Recovered original secret

What I Learned:

Encoding is not encryption
Obfuscation is not security
Level 9 → 10

Goal: Retrieve the next password

Work:

Reviewed source code
Identified unsanitized user input in shell command
Manipulated command execution
Retrieved password

Vulnerability: Command Injection

What I Learned:

User input inside shell commands is extremely dangerous
Command Injection can lead to full system compromise
Level 10 → 11

Goal: Bypass filtering

Work:

Analyzed blacklist restrictions
Manipulated application behavior without blocked characters
Retrieved password

Vulnerability: Argument Injection

What I Learned:

Blacklists are unreliable
Input validation must be designed properly
Level 11 → 12

Goal: Display the password

Work:

Analyzed encrypted cookie structure
Recovered XOR key
Modified cookie contents
Generated valid forged cookie

Vulnerability: XOR Cookie Forgery

What I Learned:

Encryption without integrity protection is weak
Client-side trust is dangerous
Level 12 → 13

Goal: Upload executable code

Work:

Analyzed upload functionality
Modified hidden filename parameter
Uploaded PHP payload
Executed uploaded file
Retrieved password

Vulnerability: Unrestricted File Upload

What I Learned:

Hidden form fields are user-controlled
File uploads require strict server-side validation
Key Skills Gained
Source Code Review
Directory Enumeration
Cookie Manipulation
HTTP Request Tampering
Local File Inclusion (LFI)
Command Injection
Argument Injection
XOR Cryptanalysis
Cookie Forgery
File Upload Exploitation
Web Application Testing
Biggest Lesson From Natas 0–12

Every level was solved because the application trusted something it shouldn't have:

Level	Trusted Thing
0	Hidden HTML
1	Browser Restrictions
2	Hidden Directory
3	robots.txt
4	Referer Header
5	Cookie
6	Source File
7	URL Parameter
8	Encoded Secret
9	User Input
10	Blacklist Filter
11	Client Cookie
12	Hidden Form Field

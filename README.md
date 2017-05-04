Book_Downloader.py is a Python program that downloads e-books available on the website libgen.io. (Libgen.io is the largest collection of e-books on the web.) E-books of the following formats are downloaded: epub, pdf, mobi. Only books available in English are downloaded. The following libraries have been used: urllib, urllib2, beautifulsoup. 

Requirements:
OS - Windows/Mac
Software - Python 2.7

HOW TO RUN: 
1. On line 44, change the location of the place where the books would be saved. If you want to save the book on the desktop, change the location from 'C:\Users\User_Name\Desktop\%s' to:

	Windows:    'C:\Users\"username"\Desktop\%s', where "username" is the name of the user account of your PC. 
	
	Mac:    '/Users/"username"/Desktop/%s', where "username" is the name of the user account of your PC.
	
2. Run the program
3. Type the name of the book that you want and press the enter key. 
4. Type the name of the author of the book that you want and press the enter key. 
5. If the book with the specified title and author exists on Libgen, it will be downloaded automatically. 


Authors: Navdeep Singh, Harshit Agarwal


NOTE: libgen.io can sometimes be slow to respond. This is due to the site's limited resources and huge traffic. Please do not lose patience. Your download will generally be completed within 3 minutes. If you are thinking that "If this program takes 3 minutes to download the book, why shouldn't I visit the website and download it myself?", then remember that the program is taking longer than usual to download the book because the website is slow and if you download the book manually it will take you more time than the program itself. 

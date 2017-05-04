import urllib
import urllib2
from bs4 import BeautifulSoup

def Search(title, author):      #Function to search for the book    
    while len(title) == 0:
        title = raw_input('Please enter the name of the book: ')        
    while len(author) == 0:
        author = raw_input('Please enter the name of the author: ')
    print "Searching for book..."
    title_author = title + ' ' + author        #Creates a single search term which is used to search the book
    url = 'http://libgen.io/search.php?req='
    url += urllib.quote_plus(title_author)        #Creates a search URL for Libgen
    page = urllib2.urlopen(url).read()      #Opens the search URL

    if 'view.php?id' not in page:        #Checks if there are any results on the page
        print 'Book not found.'

    else:
        print "Book found."
        soup = BeautifulSoup(page, "html.parser")      #Creates objects of every element of the webpage using the library 'Beautiful Soup'
        Contents = []    
        for sibling in soup.find("table",{"class":"c"}).tr.next_siblings:       #Extracts contents of a table with class 'c' from the HTML code of the webpage
            Contents.append(sibling)        #Adds every row of the table to the Contents list
        url, extension = DownloadURL(Contents)
        Download(url, title, extension)

def DownloadURL(Contents):          #Function to extract the URL of the page that contains the download URL
    url, extension = '', ''         
    flaglang, flagext, flag = 0, 0, 0       
    for results in range(len(Contents)):         #Iterates through every element of the Contents list     
        for i in Contents[results]:         #Iterates through every line of each element of the Contents list
            links = str(i).split('"')       #Splits every string with respect to quotation marks
            for lines in i:
                if 'English' in lines:      #Checks if the language of the book is English
                    flaglang = 1
                if 'pdf' in lines:      #Checks if the book exists in PDF format
                    flagext = 1
                    extension = '.pdf'
                elif 'epub' in lines:       
                    flagext = 1
                    extension = '.epub'
                elif 'mobi' in lines:       
                    flagext = 1
                    extension = '.mobi'
            flag = flaglang * flagext       #Checks if both conditions are true
            if flag == 1:
                for lines in links:         #Iterates through links
                    if 'ads' in lines:      #Checks if the substring 'ads' appears in links, which is the link of the webpage where the download link is present
                        url = 'http://libgen.io' + lines        #Creates a libgen download page URL
                        break
        if flag == 1:break

    return url, extension       #Returns the download page URL and file extension

def Download(url, title, extension):       #Function to download the book
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    links = soup.find_all('a')             #Finds all the links in the webpage
    for link in links:
        if 'get.php' in str(link):      #Finds the string which containts 'get.php'. This is the partial download link for the book            
            temp = str(link).split('"')         #Splits the string to extract the download URL
    dloadurl = 'http://libgen.io' + temp[1]      #Generates the complete download URL 
    print 'Downloading book...'
    dloadurl = dloadurl.replace('amp;','')       
    title = title.replace(' ','_')
    location = 'C:\Users\User_Name\Desktop\%s' %(title+extension)        #Stores the file in this location. The location needs to be changed depending on the operating system.
    urllib.urlretrieve(dloadurl, location)
    print 'Download Completed! Check your desktop'


title, author = '', ''
Search(title,author)

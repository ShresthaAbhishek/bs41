from bs4 import BeautifulSoup

#working with files in python

with open ('home.html', 'r') as html_file: #file object in python
    content = html_file.read()
    
    
    #creating an instances of bs4
    soup = BeautifulSoup(content, 'lxml')#lxml = parser method
    
    
    # courses_html_tags = soup.find_all('h5')#finds all the h5 tags
    # for course in courses_html_tags:
    #     print(course.text)    #.text attributes shows only the text of the tag
    
    course_cards = soup.find_all('div', class_ = 'card')#class is a keyword in python
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] #splitting the text within price (a) tag
        print(f"The price for {course_name} is {course_price}")
        
        
        
        
        
        
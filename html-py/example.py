#!/usr/bin/env python

import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
number = form.getvalue("number")

if number:
    result = int(number) ** 2
    print("<html>")
    print("<head>")
    print("<title>Python and HTML Example</title>")
    print("</head>")
    print("<body>")
    print("<h1>The square of %s is %s</h1>" % (number, result))
    print("</body>")
    print("</html>")
else:
    print("<html>")
    print("<head>")
    print("<title>Python and HTML Example</title>")
    print("</head>")
    print("<body>")
    print("<h1>Please enter a number</h1>")
    print("</body>")
    print("</html>")

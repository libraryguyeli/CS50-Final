# U.S. Passport Application Helper
#### Video Demo: https://youtu.be/vTUQgH_j9uc
#### Description:
I used to be a U.S. Passport Acceptance Agent at the public library that I work at. I noticed that a lot of our customers had small questions about the process
that were answered very quickly because they were such small, straight-forward questions. I saw a possible need to add a sort of helper to our website so that people
could visit that instead of calling the library and inundating our call center with calls about general questions. In early 2021 before I had ever heard of this course,
I had an idea to make a kind of passport application helper. After completing Flask in week 9, I decided I should pick it up and make it happen.

After being greeted by the homepage, you will have the option of visiting a page that will walk you through the requirements of getting a U.S. passport, complete
with external links (that open in new tabs! I'm not evil.) that give the user more detailed information straight from the U.S. State Department itself. Another
option you have is to use the cost calculator. While the U.S. State Department does have a version of this, a version that accounts for the cost of a single passport applicant,
my version is built for the total cost of a family of
passport applicants. When I was a passport agent, we would be bombarded by families getting passports for the whole family, and they often liked to pay with one
check instead of splitting the checks for individual payments. However, my version also handles individual passport applicants. Lastly, there is a page that can
show you when to expect your passport back if you apply that day.

The final project was completed in the CS50 IDE.


#### application.py
I decided to use Flask to implement my vision for the Passport Application Helper because it was robust and dynamic. I also already had some experience with
Python, and had used Flask a time or two. There are 4 functions, one each for the pages I created. There is a fifth function that I used: the usd() function
from C$50, and I gave credit to C$50 in that file. This file holds the site together. I needed it to request information from the user and to return new
information to the user in the calculator file.


#### layout.html
This was the first page I worked on. I chose blue because that's the color of a U.S. passport and I wanted to look on-brand. After trying to make it look pretty,
I realized I should just use Bootstrap and it greatly improved the appearance of the site. I had heard of Bootstrap before CS50, but I'd never used it. It's
easier than I thought it would be. The navbar is Bootstrap. I also imported some fonts that I found on Google and used that pair of fonts to provide some contrast to the page.
I used Bootstrap on the navigation bar, which is mobile-friendly because it collapses when the screen reaches a certain width.


#### styles.css
I started my stylesheet by displaying any header, nav, aside, and articles I used neatly as blocks, along with an ID that I created, calc-form. I used two different fonts, one for the headers and another for
the body of the page. I added the background header image that I created based on a free Creative Commons-licensed airplane clipart that I flipped to white from black.
I added some padding on a lot of my tags, like the list items in the navbar and the body. I had to look up online how to make the radio buttons on the requirements.html
page appear next to each other, centered, and below the label text. One final point is that it was important to me that the site be accessible on all devices, so I made the pages responsive.


#### index.html
This is the first page that I worked on after getting the layout right. This page is just a greeting page to the user explaining some things about the website
and how it works. I used this page to come up with the idea of centering everything on the site aside from the h1 tag.


#### calculator.html / calculated.html
This page takes user input from a number of fields and calculates how much money the user will owe based on the number and type of passports and services they
require. I ultimately decided to use two different HTML files to acquire the data and to display the results because I am admittedly on a bit of a time crunch
(I started the course a little after the start date) and I have enough experience with Python and HTML to use that as opposed to Javascript. I set the minimum
values that it will accept to 0 to avoid errors.


#### eta.html
This was the second page that I started with and it was the quickest page for me to complete. I used the datetime library in the application.py file. It takes the
current date from the system and provides 5, 7, 8 and 11 weeks away from today's date as a result. As far as I know, this is the most straight-forward way I could
have done this, and it was very easy.


#### requirements.html / checklist.html
This was the last page I did and the most challenging. I tried to use Python and Flask to create responses to radio buttons being selected, but I realized pretty
quickly that I would need to use JavaScript. I had no experience with JavaScript before taking this class, so it took me a little while to go back through the
lecture and understand how to change the inner HTML of a page. I also went back and studied the Problem Set 8 assignment for help, since I changed some of the inner
HTML in that assignment.

Basically, the requirements page asks if you have had a passport before and lets you know how you need to apply. If you have had a passport
and it's not expired or expired less than 5 years ago, your journey ends here with a link to more information from the State Department. But if it is your first
passport or you're ineligible for renewal, you are presented with a button that takes you to a checklist. I originally wanted to have it all on one page where the
questions pop up after the prior question has been answered, but my JavaScript isn't strong enough. So I decided to make a separate page with the other questions.
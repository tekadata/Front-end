 Flour Shower 

  Project objectives

    Develop web pages according to mockups
    Build responsive web pages
    Factor your HTML & CSS code

Now that you have learnt basic HTML & CSS moves, you can build your first website from mockups.

Git repository:
https://gitlab.matrice.io/flour-shower/tkiener-flour-shower

 Introduction

Now that you have learnt some basic HTML and CSS, let’s use your toolbox on an actual project.

For a week, you will do the typical job of a front-end developer: a design/marketing team has given you mockups, and it’s your job to turn the visuals into actual web pages.
Expectations

You need to produce web pages that are:

    Perfect implementation of the visuals provided (the designer intentionally placed each element, your job is not to re-design but to faithfully implement!)
    Fully responsive
    Of excellent code quality

Organisation

We have cut down the project into steps. 
Each step has a few points dedicated to code quality, so be sure to spend one hour or two cleaning up your code for each step.

There’s no Sentinel for this project, so in theory you are free to organise your files however you want.

That being said, we recommend you to have the following file architecture:

    All your HTML files at the root of your repository
    A stylesheets folder with your CSS files (you can have one file for the properties shared by all pages -such as the styling of the layout- and one additional CSS file per page)
    An images folder with all the image files

This is a standard way of organising files for a small web project like this one, and it ensures that anybody looking at your code knows where to find what.

Assets

Here are the images used in the mockups. You'll need them to build the web pages.
>>> assets.zip

Step 1 



Without further ado, let’s discover the website you will code this week.

It’s called Flour Shower, and it’s the website for a bakery!

(Because who doesn’t want looking at pastries for a full week.)

Files:

step1 - screenshot - width 500.png

step1 - screenshot - width 750.png

step1 - screenshot - width 1280.png

 Step 2

Let’s move on to the next page.

Files:

step2 - screenshot - width 500.png

step2 - screenshot - width 750.png

step2 - screenshot - width 1280.png



There’s not a lot happening in this page, but there are two things to pay attention to if you want to produce clean code.

    Look at how the page’s top section looks exactly like the top section on the homepage! Surely you can re-use what you have done on step 1. Maybe have a top-section class that styles a page’s main title and its subtitle?

    Look at the difference between the mobile and the desktop version in how the images are aligned. A clean way to code this would be to have no information about “right/left” alignment in the HTML, and to handle this purely in CSS, using grid and media queries. Look at the pseudo-class nth-of-type, it might help.

Code quality

Don’t forget to spend one or two hours cleaning up your code, as each step has points for code quality.

 Step 3

There’s not one page, but two pages for this step.

Files:

step3 - screenshot - width 500.png

step3 - screenshot - width 750.png

step3 - screenshot - width 1280.png



However, as you can see, they look eerily similar!

So your job for this step is to write elegant CSS code to style both pages. Your CSS must be completely shared between the two pages - don’t repeat yourself!
Code quality

Don’t forget to spend one or two hours cleaning up your code, as each step has points for code quality.

 Step 4

Finally, let’s wrap things up with the contact page.

Files:

step4 - screenshot - width 500.png

step4 - screenshot - width 750.png

step4 - screenshot - width 1280.png

If you can, have a look on how to embed the GoogleMaps information. Otherwise, you can use the maps found in the assets.

Code quality

Don’t forget to spend one or two hours cleaning up your code, as each step has points for code quality.


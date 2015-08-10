Title: Getting started with Pelican
Category: Python

I've decided to learn how to generate static sites with Pelican! After previously using Jinja to help build sites, both with Flask and on its own, this is going pretty smoothly. It's nice that the themes are based on Jinja, a highly intuitive templating language, so you can easily alter templates to your liking. But the great thing about Pelican is that, by default, templates have access to various Pelican-specific variables as well as the variables that you set in your configuration file, so you often don't even need to touch the template files themselves to customize their content.

Also, being able to generate HTML from Markdown files makes writing content much simpler, even if it only means not having to type the few extra tags you'd need to use in Jinja templates. Easy syntax highlighting is an added bonus. All you have to do to get Python syntax highlighting for a block of code is add `:::python` right above it.

Fortunately for me, it seems that some of the awkward features of Pelican that other users had to deal with in the past have been ironed out in more recent versions. For instance, since [version 3.3](http://blog.getpelican.com/pelican-3.3-released.html), you can keep a Git repository in your output folder without risking destroying it whenever you regenerate your site. If you specify the following in your configuration file, everything but your `.git` directory will be erased when you make any updates:

    :::python
    DELETE_OUTPUT_DIRECTORY = True
    OUTPUT_RETENTION = ['.git']

The whole process of making a site with Pelican is relatively pain-free, especially since the `pelican` command line tool has reasonable defaults for the output folder (`output`) and the configuration file (`pelicanconfig.py`), and `pelican-quickstart` sets `content` as the path to your content directory, so you usually only need to enter `pelican` to update your site when you're developing. I only felt the need to write a simple batch script that starts up `python -m http.server` in the output directory without regenerating the site, unlike the `develop_server.sh` script that `pelican-quickstart` gives you. Overall, I'm glad I took the time to see for myself why Pelican is the most popular static site generator for Python.

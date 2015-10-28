Title: Standalone uWSGI
Category: Python

At my lab, we're preparing to host [jsPysch](http://www.jspsych.org) experiments online, and we had some unused computers sitting around, so we decided to use one of them as a server for collecting experiment data. We won't be using it to serve static content since everything else will be hosted on GitHub Pages, so I figured we could run [uWSGI](https://uwsgi-docs.readthedocs.org) in standalone mode instead of putting it behind Nginx. It's fairly easy to set up with Flask. After installing all of the dependencies, you just need to make a uWSGI configuration file similar to the following:

    :::ini
    [uwsgi]

    master = true
    http = 0.0.0.0:80
    http-to = /tmp/uwsgi.sock
    socket = /tmp/uwsgi.sock

    module = flask_module_name_here
    callable = application_variable_name_here

    uid = user_id_here
    gid = group_id_here
    chown-socket = user_id_here

If the file is named `server.ini`, you can start the server by entering `sudo uwsgi --ini server.ini` on the command line. After that, you can start making HTTP requests to your domain (your IP address).

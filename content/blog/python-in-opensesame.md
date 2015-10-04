Title: Python in OpenSesame
Category: Python

At my lab, I've been using [OpenSesame](http://osdoc.cogsci.nl) to create computer-based behavioral experiments lately. Normally, we'd use proprietary software like E-Prime and Inquisit, which usually work well for what we need to do. However, E-Prime has some serious bugs (One time, when it crashed, it completely erased an experiment file I was working on without a trace), Inquisit's syntax is limited enough that I often end up writing Python scripts to generate pieces of extremely repetitive Inquisit code, and both E-Prime and Inquisit don't make it very easy to arrange your own graphical layouts.

OpenSesame, on the other hand, is open source and uses Python as its back end. It has its share of minor bugs, but the ability to write parts of experiments in Python instead of using the E-Prime-like GUI is definitely worth it. For example, you can write something like the following for the audio presentation and response screen for a standard [tritone paradox](http://deutsch.ucsd.edu/psychology/pages.php?i=206) paradigm:

    :::python
    import os
    import re
    from libopensesame import widgets
    from openexp.sampler import sampler

    overall_responses = eval(exp.get('overall_responses'))
    first_note = self.get('first_note')

    audio_folder = 'Tritone Stimuli'
    audio_file = os.path.join(audio_folder, first_note + '.wav') 

    audio = sampler(exp, exp.get_file(audio_file))
    form = widgets.form(exp, cols=2, rows=2, theme='')

    form.render()
    self.sleep(1000)
    audio.play(block=True)
    self.sleep(1000)

    label = widgets.label(form, text='Was the second note lower or higher than the first note?')
    form.set_widget(label, (0, 0), colspan=2)

    template = '<span color="white">%s</span>'
    low_button = widgets.button(form, text=template % 'lower', var='response')
    form.set_widget(low_button, (0, 1))
    hi_button = widgets.button(form, text=template % 'higher', var='response')
    form.set_widget(hi_button, (1, 1))

    t1 = self.time()
    response = form._exec()
    rt = self.time() - t1

    response = re.sub(r'<[^>]*>', '', response)
    self.set_response(response=response, response_time=rt)

    direction = 'up' if response == 'higher' else 'down'
    overall_responses[first_note + '_' + direction] += 1
    exp.set('overall_responses', overall_responses)

This displays a blank screen, plays an audio file containing two sequential [Shepard tones](https://en.wikipedia.org/wiki/Shepard_tone) a tritone apart, then displays a response form where the upper half prompts the participant to select whether they heard the second note as lower or higher and the bottom half has two buttons that allow them to choose. Having access to standard grid placement functions and built-in buttons that wait for mouse clicks greatly simplifies this task, which would otherwise require coding a canvas with a mouse listener that only responds to clicks within certain coordinates on the screen after the sound file finishes playing. If you wanted, you could even set the buttons and use `form.render()` before playing the audio file to have the buttons show up first without allowing any responses until you run `form._exec()`, which is what we're doing in a different but related experiment.

By default, the return value for a button click is the button's text, including its HTML, but since this is Python, you can easily use regular expression substitution to remove any HTML tags (`response = re.sub(r'<[^>]*>', '', response)`). The only annoying thing in all of this is that when you save a Python dictionary (`overall_responses` in this case) as an experiment-wide global variable using `exp.set()`, OpenSesame converts it into a string, so you need to use `eval()` to turn it back into a dictionary when you access it with `exp.get()`. However, being able to keep track of many counters in one variable this way instead of splitting them up into different variables is still very convenient since the entire dictionary is recorded under a single column in the log file.

Of course, having access to for loops (Why doesn't Inquisit have normal for loops?) makes it trivially easy to code a final summary screen with several columns and many rows:

    :::python
    from libopensesame import widgets

    notes = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
    columns = ('<b>1st note</b>', '2nd note lower', '2nd note higher')
    overall_responses = eval(exp.get('overall_responses'))

    form = widgets.form(exp, cols=3, rows=14, theme='')

    for i in range(3):
        label = widgets.label(form, text=columns[i])
        form.set_widget(label, (i, 0))

    for i in range(12):
        row_num = i + 1
        note = notes[i]
        note_label = widgets.label(form, text=note)
        form.set_widget(note_label, (0, row_num))
        down = str(overall_responses[note + '_down'])
        down_label = widgets.label(form, text=down)
        form.set_widget(down_label, (1, row_num))
        up = str(overall_responses[note + '_up'])
        up_label = widgets.label(form, text=up)
        form.set_widget(up_label, (2, row_num))

    button = widgets.button(form, text='<span color="red">EXIT</span>')
    form.set_widget(button, (1, 13))

    form._exec()

Python is wonderful.

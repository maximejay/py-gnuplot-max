.. meta::
   :description: gnuplot plotting backend for python.
   :keywords: gnuplot, py-gnuplot, pandas, python, plot

Gnuplot is a portable command-line driven graphing utility for many
platforms. To leverage the powful gnuplot to plot beautiful image in
efficicent way in python, we port gnuplot to python. Let's see an example
at first:

..
    cmd2img:: python3
    :image: simple.1.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    g = gnuplot.Gnuplot(terminal = 'pngcairo font "arial,10" fontscale 1.0 size 600, 400',
                        output = '"simple.1.png"')
    g.plot('[-10:10] sin(x)',
           'atan(x)',
           'cos(atan(x))',
           key = 'fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid',
           style = 'increment default',
           samples = '50, 50',
           title = '"Simple Plots" font ",20" norotate')

From the example we can see, we plot the function with plot() function,
with all the options as the function parameters. It's easy to understand
and comply with both gnuplot and python's grammer. The generated image is as
below:

.. figure:: http://gnuplot.sourceforge.net/demo/simple.1.png 
   :width: 350

   figure 1. pygnuplot demo 1: simple function

Let's see the detail in the below:

.. contents:: [Contents]
   :depth: 3

1. Introduction and examples list
===================================

As we know Gnuplot is a portable and powerful command-line driven graphing
utility for many platforms. To leverage the power of Gnuplot, We develop
the py-gnuplot in a easy understand way.

**py-python only support python3** since the function dictionary paramaters in
python2 is not in order.

This package has an object-oriented design as well as direct function call to
allows the user flexibility to set plot options and to run multiple gnuplot
sessions simultaneously.

We will introduce it in detail in the following chapter and here list the
exaples used in this article as below:

.. _Table1:

.. list-table:: Table1 : A demostration of pygnuplot.gnuplot script
   :widths: 15, 20, 20, 70
   :header-rows: 1

   * - gnuplot demo script
     - object-oriented interface script
     - direct function call script
     - All the script produce the same image
   * - `simple.dem`_
     - simple2.py_
     - simple3.py_
     - |simple.1.png|
   * - `surface2.dem`_
     - surface1.py_
     - surface2.py_
     - |surface2.9.png|
   * - `iterate.dem`_
     - whale1.py_
     - whale2.py_
     - |whale.png|

.. _Table2:

.. list-table:: Table 2: A demostration of plot() and plot_data()
   :widths: 15, 20, 20, 70
   :header-rows: 1

   * - gnuplot demo script
     - object-oriented interface script
     - direct function call script
     - All the script produce the same image
   * - `histo.1.gnu`_
     - histo.1.py_
     - histo.2.py_
     - |histograms.1.png|
   * - `finance.dem`_
     - finance1.py_
     - finance1.py_
     - |finance.13.png|

.. list-table:: Table 3: Examples porting from Matplotlib
   :widths: 35, 35, 35, 35
   :header-rows: 0

   * - `3.2.1 Stacked bar chart`_ |sphx_glr_bar_stacked_001.png|
     - `3.2.2 Grouped bar chart with labels`_ |sphx_glr_barchart_001.png|
     - `3.2.3 Multiplot Axes Demo`_ |sphx_glr_axes_demo_001.png|
     - `3.2.4 control view and zoom`_ |sphx_glr_axes_margins_001.png|
   * - `3.2.5 Rendering math equation using TeX`_ |sphx_glr_tex_demo_001.png|
     - `3.2.6 Basic pie chart`_ |sphx_glr_pie_features_0011.png|
     - 
     - 

.. _simple.dem: http://gnuplot.sourceforge.net/demo/simple.1.gnu
.. _surface2.dem: http://gnuplot.sourceforge.net/demo/surface2.9.gnu
.. _histo.1.gnu: http://gnuplot.sourceforge.net/demo/histograms.1.gnu
.. _iterate.dem: http://gnuplot.sourceforge.net/demo/iterate.2.gnu
.. _finance.dem: http://gnuplot.sourceforge.net/demo/finance.13.gnu
.. |simple.1.png| image:: http://gnuplot.sourceforge.net/demo/simple.1.png
   :width: 180
.. |surface2.9.png| image:: http://gnuplot.sourceforge.net/demo/surface2.9.png
   :width: 180
.. |finance.13.png| image:: http://gnuplot.sourceforge.net/demo/finance.13.png
   :width: 180
.. |iterate.2.png| image:: http://gnuplot.sourceforge.net/demo/iterate.2.png
   :width: 180
.. |whale.png| image:: http://ayapin-film.sakura.ne.jp/Gnuplot/Pm3d/Part1/whale.png
   :width: 180
.. |histograms.1.png| image:: http://gnuplot.sourceforge.net/demo/histograms.1.png
   :width: 180
.. |sphx_glr_bar_stacked_001.png| image:: https://matplotlib.org/_images/sphx_glr_bar_stacked_001.png
   :width: 180
.. |sphx_glr_barchart_001.png| image:: https://matplotlib.org/_images/sphx_glr_barchart_001.png
   :width: 180
.. |sphx_glr_axes_demo_001.png| image:: https://matplotlib.org/_images/sphx_glr_axes_demo_001.png
   :width: 180
.. |sphx_glr_pie_features_0011.png| image:: https://matplotlib.org/_images/sphx_glr_pie_features_0011.png
   :width: 180
.. |sphx_glr_tex_demo_001.png| image:: https://matplotlib.org/_images/sphx_glr_tex_demo_001.png
   :width: 180
.. |sphx_glr_axes_margins_001.png| image:: https://matplotlib.org/_images/sphx_glr_axes_margins_001.png
   :width: 180


2. Plot elements in py-gnuplot
=================================

As we know, gnuplot use commands to plot all kinds of image, we port almost
all the useful commands as functions in py-gnuplot.

In `2.1 member functions port from Gnuplot`_ we introduce the member
functions that we can plot all what Gnuplot could do, The limitation is
it's not so easy to plot the python generated data with the those existing
command.

To plot the data generated in python, we develop additional functions as
below, ::

    plot_data(self, data, *items, **kwargs):
    splot_data(self, data, *items, **kwargs)

they are almost the same as the original plot()/splot(), the difference is
we pass the data as the first parameter, you don't give the filename in the
plot command, see detail in `2.2 new developed member functions for python
generated data`_ .

Sometime we only need simple plot and don't want to allocate a Gnuplot
instance, we develop the easy way to plot: `2.3 new developed global
class-less function call`_ and you can plot the image in a easy way with
global class-less function call.

2.1 member functions port from Gnuplot
---------------------------------------

The principle is if you can write Gnuplot script, you can write py-gnuplot.
There is 1-1 mapping between almost all Gnuplot command and python
function;

2.1.1 The constructor
+++++++++++++++++++++

.. code-block:: python

    def __init__(self, *args, log = False, **kwargs):
        '''
        *args: The flag parameter in gnuplot
        log: If print the gnuplot log
        **kwargs: the flag that need to be set. You can also set them in the set() function.
        '''

When create the Gnuplot instance, you can pass some parameter to it, you
can also set them when you call set() or plot(), they are the same.

The "log" parameter is a new added flag to indicate if we print the gnuplot
execution log when run. For example:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    #http://ayapin-film.sakura.ne.jp/Gnuplot/Pm3d/Part1/whale.html
    g = gnuplot.Gnuplot(log = True,
            term = 'pngcairo size 480,480',
            out = '"whale.png"',
            style = 'line 100 lw 0.1 lc "black"',
            pm3d = 'depth hidden3d ls 100',
            cbrange = '[-0.5:0.5]',
            palette = 'rgb -3,-3,-3',
            colorbox = None,
            border = None,
            key = None,
            zrange = '[-2:2]',
            tics = None,
            view = '60,185,1.5')
    g.splot('"examples/whale.dat" w pm3d')

    # Or the options could be passed on the constructor, it could be writen
    # as:
    g = gnuplot.Gnuplot(log = True)
    g.splot('"examples/whale.dat" w pm3d',
            term = 'pngcairo size 480,480',
            out = '"whale.png"',
            style = 'line 100 lw 0.1 lc "black"',
            pm3d = 'depth hidden3d ls 100',
            cbrange = '[-0.5:0.5]',
            palette = 'rgb -3,-3,-3',
            colorbox = None,
            border = None,
            key = None,
            zrange = '[-2:2]',
            tics = None,
            view = '60,185,1.5')

This is the script output with the log=True::

    [py-gnuplot] set term pngcairo size 480,480
    [py-gnuplot] set out "whale.png"
    [py-gnuplot] set style line 100 lw 0.1 lc "black"
    [py-gnuplot] set pm3d depth hidden3d ls 100
    [py-gnuplot] set cbrange [-0.5:0.5]
    [py-gnuplot] set palette rgb -3,-3,-3
    [py-gnuplot] unset colorbox
    [py-gnuplot] unset border
    [py-gnuplot] unset key
    [py-gnuplot] set zrange [-2:2]
    [py-gnuplot] unset tics
    [py-gnuplot] set view 60,185,1.5
    [py-gnuplot] splot "examples/whale.dat" w pm3d

And this is the image output: |small_whale.png|

.. |small_whale.png| image:: http://ayapin-film.sakura.ne.jp/Gnuplot/Pm3d/Part1/whale.png
   :width: 50

2.1.2 cmd()
+++++++++++

.. code-block:: python

    def cmd(self, *args):
        '''
        *args: all the line that need to pass to gnuplot. It could be a
        list of lines, or a paragraph; Lines starting with "#" would be
        omitted. Every line should be a clause that could be executed in
        gnuplot.
        '''

We implemented the function cmd() and pass the command to call Gnuplot to
plot the data, Thus we could do everything with the only one simple
function:

.. _simple1.1.py:
..
    cmd2img:: python3
    :image: simple.1.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    # Illustration of object-oriented interface, you can see we only wrap the
    # gnuplot script by g.cmd('...') and it's simple and straitfoward if you
    # are familar with Gnuplot.
    g = gnuplot.Gnuplot()
    g.cmd('set terminal pngcairo font "arial,10" fontscale 1.0 size 600, 400')
    g.cmd('set output "simple.1.png"')
    g.cmd('set key fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid')
    g.cmd('set style increment default')
    g.cmd('set samples 50, 50')
    g.cmd('set title "Simple Plots" ')
    g.cmd('set title  font ",20" norotate')
    g.cmd('plot [-10:10] sin(x),atan(x),cos(atan(x))')

Or you can even pass the Gnuplot command as a string list or a text paragraph:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    # Illustration of object-oriented interface, you can see we only wrap the
    # gnuplot script by g.cmd('...') and it's simple and straitfoward if you
    # are familar with Gnuplot.
    g = gnuplot.Gnuplot()

    # Take all the Gnuplot command as a list of command:
    g.cmd('set terminal pngcairo font "arial,10" fontscale 1.0 size 600, 400',
    'set output "simple.1.png"',
    'set key fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid',
    'set style increment default',
    'set samples 50, 50',
    'set title "Simple Plots" ',
    'set title  font ",20" norotate',
    'plot [-10:10] sin(x),atan(x),cos(atan(x))')

    # Take all the Gnuplot command as a script paragraph:
    plot_cmd = '''
    set terminal pngcairo font "arial,10" fontscale 1.0 size 600, 400
    set output "simple.1.png"
    set key fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid
    set style increment default
    set samples 50, 50
    set title "Simple Plots
    set title  font ",20" norotate
    plot [-10:10] sin(x),atan(x),cos(atan(x))'''
    g.cmd(plot_cmd)

This is the image output: |small_simple.png|

.. |small_simple.png| image:: http://gnuplot.sourceforge.net/demo/simple.1.png
   :width: 50

By this way we can do everything that Gnuplot can do and cannot do what
Gnuplot itself can't do. It's the exact way that the Gnuplot do it. and we
don't get any benifit besides we can call Gnuplot in python. So we develop
many other functions as below:

2.1.3 set()
+++++++++++

.. code-block:: python

    def set(self, *args, **kwargs):
        '''
        *args: options without value
        *kwargs: options with value. The set and unset commands may optionally
                 contain an iteration clause, so the arg could be list.
        '''

The set command can be used to set lots of options. The set and unset
commands may optionally contain an iteration clause, so the arg could be
list. For examples:

We set the options before plot and then call plot to render the image. It's
equivalent to example in `2.1.2 cmd()`_ but seems muck like a python script.

.. _simple2.py:

..
    cmd2img:: python3
    :image: simple.1.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot


    # Gnuplot lines:
    #set terminal pngcairo font "arial,10" fontscale 1.0 size 600, 400
    #set output "simple.1.png"
    #set key fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid
    #set style increment default
    #set samples 50, 50
    #set title "Simple Plots" font ",20" norotate

    g = gnuplot.Gnuplot()
    g.set(terminal = 'pngcairo font "arial,10" fontscale 1.0 size 600, 400',
            output = '"simple.1.png"',
            key = 'fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid',
            style = 'increment default',
            samples = '50, 50',
            title = '"Simple Plots" font ",20" norotate')
    g.plot('[-10:10] sin(x),atan(x),cos(atan(x))')

set() is flexible but indeed set() functions is not necessary. We could
pass the options as parameter in the constructor and plot(). For examples
the following script act equally with the above:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    # py-python lines:
    g = gnuplot.Gnuplot(terminal = 'pngcairo font "arial,10" fontscale 1.0 size 600, 400',
                        output = '"test.png"',
                        boxwidth = '0.9 relative',
                        style = 'fill solid 1.0',
                        label = ['"y=x" at 1,2',
                                 '2 "S" at graph 0.5,0.5 center font "Symbol,24"',
                                 '3 "y=x^2" at 2,3,4 right'])
    g.plot('"file.dat" with boxes')

We can also write it as the following, they are all the same:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    # py-python lines:
    g = gnuplot.Gnuplot()
    g.plot('"file.dat" with boxes',
           terminal = 'pngcairo font "arial,10" fontscale 1.0 size 600, 400',
           output = '"test.png"',
           boxwidth = '0.9 relative',
           style = 'fill solid 1.0',
           label = ['"y=x" at 1,2',
                    '2 "S" at graph 0.5,0.5 center font "Symbol,24"',
                    '3 "y=x^2" at 2,3,4 right'])

2.1.4 unset()
+++++++++++++++

.. code-block:: python

    def unset(self, *items):
        '''
        *args: options that need to be unset
        '''

Options set using the set() function may be returned to their default state by
the corresponding unset() function:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    # py-python lines:
    g = gnuplot.Gnuplot()
    g.unset('xlabel', 'ylabel', 'xrange', 'yrange')
    g.plot('sin(x) with lp')

unset command could be replaced as set, for example the above example could
also be writen as:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    # Another means to unset options:
    g = gnuplot.Gnuplot()
    g.set('noxlabel', 'noylabel', 'noxrange', 'noyrange')
    g.plot('sin(x) with lp')

    # Another means to unset options:
    g = gnuplot.Gnuplot()
    g.set(xlabel = None,
          ylabel = None,
          xrange = None,
          yrange = None)
    g.plot('sin(x) with lp')

2.1.5 plot()
++++++++++++

.. code-block:: python

    def plot(self, *items, **kwargs):
        '''
        *items: The list of plot command;
        **kwargs: The options that would be set before the plot command.
        '''

plot is the primary command for drawing plots with gnuplot, We port it as a
function in py-python. As description, the plot-element is passed as
variable parameters, and options are passed as dictionary parameter. please
be noted that the plot-element should be in the single quotes:

Note that the plot()/splot() only plot the gnuplot functions and file, if
you'd like to plot data generated in python, you should call the new added
functions: `2.2.1 plot_data()`_ and `2.2.2 splot_data()`_ .

for example plot the gnuplot function or datafile we use pygnuplot.gnuplot:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    g = gnuplot.Gnuplot()
    g.plot('[-10:10] sin(x)',
           'atan(x)',
           'cos(atan(x))',
           terminal = 'pngcairo font "arial,10" fontscale 1.0 size 600, 400',
           output = '"simple.1.png"',
           key = 'fixed left top vertical Right lt black linewidth 1.000 dashtype solid',
           style = 'increment default',
           samples = '50, 50',
           title = '"Simple Plots" font ",20" norotate')

If we plot the python generated data we use plot_data() and splot_data():

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    # usage examples, please note that we didn't give the output so could only
    # see the image flash on the screen. Will introduce how to output the
    # image to files.
    df = pd.DataFrame(data = {'col1': [1, 2],
                              'col2': [3, 4],
                              'col3': [5, 6]})
    g = gnuplot.Gnuplot()
    g.plot_data(df, 'using 1:2 with lines', 'using 1:3 with points')

As we stated in `2.1.3 set()`_ , we can use parameter to replace
set()/unset() in plot() function, here is something we need to know when
using parameter to replace set()/unset():

1) If it's flag parameter, for example::

    set grid
    set hidden3d

we can pass it as a empty value:

.. code-block:: python

    #!/usr/bin/env python3

    # Examples of gnuplot.plot()
    g = gnuplot.Gnuplot()
    g.plot('sin(x)',
           'cos(x)',
           ...,
           grid = '',
           hidden3d = '',
           ...)

    # Examples of plot_data()
    df = pd.DataFrame(data = {'col1': [1, 2],
                              'col2': [3, 4],
                              'col3': [5, 6]})
    g = gnuplot.Gnuplot()
    g.plot_data(df, 'using 1:2 with lines', 'using 1:3 with points',
           grid = '')

2) We have two means to pass "unset" command, one is the no-xxx option and
   the other is xxx = None, for examples we'd like to unset the grid and
   xrange::

    unset grid
    unset xrange

We can do that in py-gnuplot by:

.. code-block:: python

    g = gnuplot.Gnuplot()
    # Example of use no-xxx to unset the flag
    g.plot(df, 'using 0:2:3:4:5 notitle with financebars lt 8',
            ...,
            nogrid = '',
            noxlabel = '',
            ...)

    # Example of use None to unset the flag
    g.plot(df, 'using 0:2:3:4:5 notitle with financebars lt 8',
            ...,
            grid = None,
            xlabel = None,
            ...)

3) If there is multiple lines for one options, for exampe in gnuplot it
   is::

    set arrow from 5,-5,-1.2 to 5,5,-1.2 lt -1
    set arrow from 5,6,-1 to 5,5,-1 lt -1
    set arrow from 5,6,sinc(5,5) to 5,5,sinc(5,5) lt -1

We pass them by a list of options:

.. code-block:: python

    g = gnuplot.Gnuplot()
    g.plot(df,
           'using 0:2:3:4:5 notitle with financebars lt 8',
           ...,
           arrow = ['from 5,-5,-1.2 to 5,5,-1.2 lt -1',
                    'from 5,6,-1 to 5,5,-1 lt -1',
                    'from 5,6,sinc(5,5) to 5,5,sinc(5,5) lt -1'],
           ...,
           ...)

2.1.6 splot()
+++++++++++++

.. code-block:: python

    def splot(self, *items, **kwargs):
        '''
        *items: The list of plot command;
        **kwargs: The options that would be set before the plot command.
        '''

The usage of splot() is exactly the same as plot().

2.2 new developed member functions for python generated data
--------------------------------------------------------------

We develop the following memember functions, they are very familar with the
orignal plot() and splot(), the only difference is that , in the new
developed function, we pass the python generated data as the first
parameter and remove the corresponding element in the plot command.

2.2.1 plot_data()
+++++++++++++++++

.. code-block:: python

    def plot_data(self, data, *items, **kwargs):
        '''
        data: The data that need to be plotted. It's either the string of list
        or the Pnadas Dataframe, if it's Pnadas Dataframe it would be converted
        to string by data.to_csv(). Note that we will execut a extra command
        "set datafile separator "," to fit the data format of csv.
        *items: The list of plot command;
        **kwargs: The options that would be set before the plot command.
        '''

The usage is the same as in `2.1.5 plot()`_ except that you should pass the
data(string or pandas Dataframe format) as the first parameter, and remove
the corresponding filename in every plot line. Moreover, the defaulst
seperator now is "," for easy use with csv file:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    # usage examples, please note that we didn't give the output so could only
    # see the image flash on the screen. Will introduce how to output the
    # image to files.
    df = pd.DataFrame(data = {'col1': [1, 2],
                              'col2': [3, 4],
                              'col3': [5, 6]})
    g = gnuplot.Gnuplot()
    # Note that the first parameter is df and there is no "data.file" in
    # the following commmand.
    g.plot_data(df,
                'using 1:2 with lines',
                'using 1:3 with points')

2.2.2 splot_data()
++++++++++++++++++

.. code-block:: python

    def splot_data(self, data, *items, **kwargs):
        '''
        data: The data that need to be plotted. It's either the string of list
        or the Pnadas Dataframe, if it's Pnadas Dataframe it would be converted
        to string by data.to_csv(). Note that we will execut a extra command
        "set datafile separator "," to fit the data format of csv.
        *items: The list of plot command;
        **kwargs: The options that would be set before the plot command.
        '''

The usage is the same as in `2.2.1 plot_data()`_ .

2.3 new developed global class-less function call
----------------------------------------------------

We can plot the image just by the above object-oriented interface, but
sometimes we want to quick plot an image in quick mode, we can call the
global class-less function call:

2.3.1 plot()
++++++++++++

.. code-block:: python

    #submodule gnuplot
    def plot(*args, **kwargs):
        '''
        *items: The list of plot command;
        **kwargs: The options that would be set before the plot command.
        '''

The usage is the same as in `2.1.5 plot()`_ except that you needn't
allocate a Gnuplot() instance at first:.

.. _simple3.py:

..
    cmd2img:: python3
    :image: simple.1.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    gnuplot.plot('[-10:10] sin(x)',
           'atan(x)',
           'cos(atan(x))',
           terminal = 'pngcairo font "arial,10" fontscale 1.0 size 600, 400',
           output = '"simple.1.png"',
           key = 'fixed left top vertical Right lt black linewidth 1.000 dashtype solid',
           style = 'increment default',
           samples = '50, 50',
           title = '"Simple Plots" font ",20" norotate')

2.3.2 splot()
++++++++++++++

.. code-block:: python

    #submodule gnuplot
    def splot(*args, **kwargs):
        '''
        *items: The list of plot command;
        **kwargs: The options that would be set before the plot command.
        '''

The usage is the same as in `2.1.6 splot()`_ except that you needn't
allocate a Gnuplot() instance at first:

2.3.3 plot_data()
+++++++++++++++++

.. code-block:: python

    def plot_data(data, *items, **kwargs):
        '''
        data: The data that need to be plotted. It's either the string of list
        or the Pnadas Dataframe, if it's Pnadas Dataframe it would be converted
        to string by data.to_csv()
        *items: The list of plot command;
        **kwargs: The options that would be set before the plot command.
        '''

The usage is the same as in `2.2.1 plot_data()`_ except that you needn't
allocate a Gnuplot() instance at first:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    df = pd.DataFrame(data = {'col1': [1, 2],
                              'col2': [3, 4],
                              'col3': [5, 6]})
    gnuplot.plot_data(df,
                      'using 1:2 with lines',
                      'using 1:3 with points')

2.3.4 splot_data()
++++++++++++++++++

.. code-block:: python

    class gnuplot.Gnuplot(object):

        def splot(self, *items, **kwargs):
            '''
            *items: The list of plot command;
            **kwargs: The options that would be set before the plot command.
            '''

The usage is the same as in `2.2.2 splot_data()`_ except that you needn't
allocate a Gnuplot() instance at first:

2.3.5 multiplot()
+++++++++++++++++

Since we don't allocate the Gnuplot instance, there is a little trick to
plot the multiplot image. To solve the issue we create 3 brand new function
to implement that, anyway, we have new options to plot the data.

.. code-block:: python

    def multiplot(\*args, \*\*kwargs):
        @args: the subplot object list;
        @kwargs: the setting options that need to be set before call plot;

    def make_plot(\*args, \*\*kwargs)
        The parameter definition is the same as plot(), but it doesn't plot
        the data really, it only return the plot dictionary for later
        multiplot() use.

    def make_splot(\*args, \*\*kwargs)
        The parameter definition is the same as splot(), but it doesn't plot
        the data really, it only return the plot dictionary for later
        multiplot() use.

    def make_plot_data (data, \*args, \*\*kwargs)
        The parameter definition is the same as plot_data(), but it doesn't
        plot the data really, it only return the plot dictionary for later
        multiplot() use.

    def make_splot_data (data, \*args, \*\*kwargs)
        The parameter definition is the same as splot_data(), but it
        doesn't plot the data really, it only return the plot dictionary
        for later multiplot() use.

Before call multiplot() we must generate the subplot object by calling
make_plot()/make_splot(), It is much like mplfinance.make_addplot(), it only
add the subplot command for further call:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    sub1 = gnuplot.make_plot('sin(x)', ylabel = 'ylabel')
    sub2 = gnuplot.make_plot('cos(x)', xlabel = 'xlabel')
    sub3 = gnuplot.make_plot('sin(2*x)', noxlabel = '', ylabel = '')
    sub4 = gnuplot.make_plot('cos(2*x)', xlabel = 'xlabel')
    gnuplot.multiplot(sub1, sub2, sub3, sub4,
                      output = '"sample.multiplot.png"',
                      term = 'pngcairo size 900,600 font ",11"',
                      multiplot  = 'layout 2,2 columnsfirst margins 0.1,0.9,0.1,0.9 spacing 0.1')

A example in reality:

.. _finance2.py:

..
    cmd2img:: python3
    :image: finance.13.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd

    # A demostration to generate pandas data frame data in python.
    df = pd.read_csv('examples/finance.dat', sep='\t', index_col = 0, parse_dates = True,
            names = ['date', 'open','high','low','close', 'volume','volume_m50',
                'intensity','close_ma20','upper','lower '])

    # make subplot at first, now there is still no real plot.
    sub1 = gnuplot.make_plot_data(df,
            'using 0:2:3:4:5 notitle with candlesticks lt 8',
            'using 0:9 notitle with lines lt 3',
            'using 0:10 notitle with lines lt 1',
            'using 0:11 notitle with lines lt 2',
            'using 0:8 axes x1y2 notitle with lines lt 4',
            title = '"Change to candlesticks"',
            logscale = 'y',
            xrange = '[50:253]',
            yrange = '[75:105]',
            format = 'x ""',
            xtics = '(66, 87, 109, 130, 151, 174, 193, 215, 235)',
            ytics = '(105, 100, 95, 90, 85, 80)',
            lmargin = '9',
            rmargin = '2',
            bmargin = '0',
            origin = '0, 0.3',
            size = ' 1, 0.7',
            grid = 'xtics ytics',
            ylabel = '"price" offset 1',
            label = ['1 "Acme Widgets" at graph 0.5, graph 0.9 center front',
                '2 "Courtesy of Bollinger Capital" at graph 0.01, 0.07',
                '3 "  www.BollingerBands.com" at graph 0.01, 0.03']
            )

    sub2 = gnuplot.make_plot_data(df,
            'using 0:($6/10000) notitle with impulses lt 3',
            'using 0:($7/10000) notitle with lines lt 1',
            ytics = '500',
            xtics = '("6/03" 66, "7/03" 87, "8/03" 109, "9/03" 130, "10/03" 151, "11/03" 174, "12/03" 193, "1/04" 215, "2/04" 235)',
            ylabel = '"volume (0000)" offset 1',
            nologscale = 'y',
            autoscale = 'y',
            size = '1.0, 0.3',
            origin = '0.0, 0.0',
            bmargin = '',
            tmargin = '0',
            format = ['x', 'y "%1.0f"'])

    # plot at one time.
    gnuplot.multiplot(sub1, sub2,
            output = '"finance.13.png"',
            term = 'pngcairo font "arial,10" fontscale 1.0 size 900, 600')

.. _3 Multiplot Axes Demo2:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd
    import numpy as np

    #https://matplotlib.org/gallery/subplots_axes_and_figures/axes_demo.html#sphx-glr-gallery-subplots-axes-and-figures-axes-demo-py
    #http://gnuplot.sourceforge.net/demo_5.2/bins.html

    # 1) create some data to use for the plot
    np.random.seed(19680801) # Fixing random state for reproducibility
    dt = 0.001
    t = np.arange(0.0, 10.0, dt)
    r = np.exp(-t / 0.05)  # impulse response
    x = np.random.randn(len(t))
    s = np.convolve(x, r)[:len(x)] * dt  # colored noise
    df = pd.DataFrame({'r': r, 'x': x, 's': s}, index = t)
    df.index.name = 't'
    #print(df.tail().to_csv())

    # 2) Plot the data
    main = gnuplot.make_plot_data(df.iloc[:1000],
            'using 1:4 with line lw 2 lc "web-blue"',
            title = '"Gaussian colored noise"',
            xlabel = '"time (s)"',
            ylabel = '"current (nA)"',
            xrange = '[0:1]',
            yrange = '[-0.015:0.03]',
            key = None,
            size = ' 1, 1',
            origin = '0, 0')
    right = gnuplot.make_plot_data(df,
            'using 4 bins=400 with boxes title "20 bins" lw 2 lc "web-blue"',
            title = '"Probability"',
            xlabel = None,
            ylabel = None,
            tics = None,
            xrange = None,
            yrange = None,
            origin = '0.65, 0.56',
            size = '0.24, 0.32',
            object = 'rectangle from graph 0,0 to graph 1,1 behind fc "black" fillstyle solid 1.0')
    left = gnuplot.make_plot_data(df,
            'using 1:2 with line lw 2 lc "web-blue"',
            title = '"Impulse response"',
            xrange = '[0:0.2]',
            origin = '0.15, 0.56',
            size = '0.24, 0.32')

    gnuplot.multiplot(main, right, left,
            output = '"sphx_glr_axes_demo_001.png"',
            term = 'pngcairo font "arial,10" fontscale 1.0 size 640, 480',
            key = '')

3. examples
============

3.1 examples port from gnuplot
------------------------------

3.1.1 finance
+++++++++++++

example with object-oriented interface call:

.. _finance1.py:

..
    cmd2img:: python3
    :image: finance.13.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd

    # A demostration to generate pandas data frame data in python.
    df = pd.read_csv('finance.dat', sep='\t', index_col = 0, parse_dates = True,
            names = ['date', 'open','high','low','close', 'volume','volume_m50',
                'intensity','close_ma20','upper','lower '])

    # Create a Gnuplot instance and set the options at first;
    g = gnuplot.Gnuplot(log = True,
            output = '"finance.13.png"',
            term = 'pngcairo font "arial,10" fontscale 1.0 size 900, 600',
            multiplot = "")

    g.plot_data(df,
            'using 0:2:3:4:5 notitle with candlesticks lt 8',
            'using 0:9 notitle with lines lt 3',
            'using 0:10 notitle with lines lt 1',
            'using 0:11 notitle with lines lt 2',
            'using 0:8 axes x1y2 notitle with lines lt 4',
            title = '"Change to candlesticks"',
            logscale = 'y',
            xrange = '[50:253]',
            yrange = '[75:105]',
            format = 'x ""',
            xtics = '(66, 87, 109, 130, 151, 174, 193, 215, 235)',
            ytics = '(105, 100, 95, 90, 85, 80)',
            lmargin = '9',
            rmargin = '2',
            bmargin = '0',
            origin = '0, 0.3',
            size = ' 1, 0.7',
            grid = 'xtics ytics',
            ylabel = '"price" offset 1',
            label = ['1 "Acme Widgets" at graph 0.5, graph 0.9 center front',
                '2 "Courtesy of Bollinger Capital" at graph 0.01, 0.07',
                '3 "  www.BollingerBands.com" at graph 0.01, 0.03']
            )

    g.plot_data(df,
            'using 0:($6/10000) notitle with impulses lt 3',
            'using 0:($7/10000) notitle with lines lt 1',
            bmargin = '',
            size = '1.0, 0.3',
            origin = '0.0, 0.0',
            tmargin = '0',
            nologscale = 'y',
            autoscale = 'y',
            format = ['x', 'y "%1.0f"'],
            ytics = '500',
            xtics = '("6/03" 66, "7/03" 87, "8/03" 109, "9/03" 130, "10/03" 151, "11/03" 174, "12/03" 193, "1/04" 215, "2/04" 235)',
            ylabel = '"volume (0000)" offset 1')

Since it enable the log options, I attach the execution log as below::

    [py-gnuplot 19:35:26] set output "finance.13.png"
    [py-gnuplot 19:35:26] set term pngcairo font "arial,10" fontscale 1.0 size 900, 600
    [py-gnuplot 19:35:26] set multiplot
    [py-gnuplot 19:35:26] set datafile separator ","
    [py-gnuplot 19:35:26] set title "Change to candlesticks"
    [py-gnuplot 19:35:26] set logscale y
    [py-gnuplot 19:35:26] set xrange [50:253]
    [py-gnuplot 19:35:26] set yrange [75:105]
    [py-gnuplot 19:35:26] set format x ""
    [py-gnuplot 19:35:26] set xtics (66, 87, 109, 130, 151, 174, 193, 215, 235)
    [py-gnuplot 19:35:26] set ytics (105, 100, 95, 90, 85, 80)
    [py-gnuplot 19:35:26] set lmargin 9
    [py-gnuplot 19:35:26] set rmargin 2
    [py-gnuplot 19:35:26] set bmargin 0
    [py-gnuplot 19:35:26] set origin 0, 0.3
    [py-gnuplot 19:35:26] set size  1, 0.7
    [py-gnuplot 19:35:26] set grid xtics ytics
    [py-gnuplot 19:35:26] set ylabel "price" offset 1
    [py-gnuplot 19:35:26] set label 1 "Acme Widgets" at graph 0.5, graph 0.9 center front
    [py-gnuplot 19:35:26] set label 2 "Courtesy of Bollinger Capital" at graph 0.01, 0.07
    [py-gnuplot 19:35:26] set label 3 "  www.BollingerBands.com" at graph 0.01, 0.03
    [py-gnuplot 19:35:26] plot $DataFrame using 0:2:3:4:5 notitle with candlesticks lt 8,\
    [py-gnuplot 19:35:26] $DataFrame using 0:9 notitle with lines lt 3,\
    [py-gnuplot 19:35:26] $DataFrame using 0:10 notitle with lines lt 1,\
    [py-gnuplot 19:35:26] $DataFrame using 0:11 notitle with lines lt 2,\
    [py-gnuplot 19:35:26] $DataFrame using 0:8 axes x1y2 notitle with lines lt 4
    [py-gnuplot 19:35:26] unset for [i=1:200] label i
    [py-gnuplot 19:35:26] set datafile separator ","
    [py-gnuplot 19:35:26] set bmargin
    [py-gnuplot 19:35:26] set size 1.0, 0.3
    [py-gnuplot 19:35:26] set origin 0.0, 0.0
    [py-gnuplot 19:35:26] set tmargin 0
    [py-gnuplot 19:35:26] set nologscale y
    [py-gnuplot 19:35:26] set autoscale y
    [py-gnuplot 19:35:26] set format x
    [py-gnuplot 19:35:26] set format y "%1.0f"
    [py-gnuplot 19:35:26] set ytics 500
    [py-gnuplot 19:35:26] set xtics ("6/03" 66, "7/03" 87, "8/03" 109, "9/03" 130, "10/03" 151, "11/03" 174, "12/03" 193, "1/04" 215, "2/04" 235)
    [py-gnuplot 19:35:26] set ylabel "volume (0000)" offset 1
    [py-gnuplot 19:35:26] plot $DataFrame using 0:($6/10000) notitle with impulses lt 3,\
    [py-gnuplot 19:35:26] $DataFrame using 0:($7/10000) notitle with lines lt 1
    [py-gnuplot 19:35:26] unset for [i=1:200] label i

And the generated output is as following:

.. image:: http://gnuplot.sourceforge.net/demo/finance.13.png
   :width: 350

3.1.2 histogram
+++++++++++++++

.. _histo.1.py:

..
    cmd2img:: python3
    :image: histograms.1.png

Plot with member functions:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd

    df = pd.read_csv('examples/immigration.dat', index_col = 0, sep='\t', comment='#')
    g = gnuplot.Gnuplot()
    g.set(terminal = 'pngcairo transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 ',
            output = '"histograms.1.png"',
            key = 'fixed right top vertical Right noreverse noenhanced autotitle nobox',
            style = 'data linespoints',
            datafile = ' missing "-"',
            xtics = 'border in scale 1,0.5 nomirror rotate by -45 autojustify norangelimit',
            title = '"US immigration from Europe by decade"')
    g.plot_data(df, 'using 2:xtic(1), for [i=3:22] "" using i ')

Since it's simple, we also could plot it with global class-less function call:

.. _histo.2.py:

..
    cmd2img:: python3
    :image: histograms.1.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd

    df = pd.read_csv('examples/immigration.dat', index_col = 0, sep='\t', comment='#')
    gnuplot.plot_data(df,
            'using 2:xtic(1), for [i=3:22] "" using i ',
            terminal = 'pngcairo transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 ',
            output = '"histograms.1.png"',
            key = 'fixed right top vertical Right noreverse noenhanced autotitle nobox',
            style = 'data linespoints',
            datafile = ' missing "-"',
            xtics = 'border in scale 1,0.5 nomirror rotate by -45 autojustify norangelimit',
            title = '"US immigration from Europe by decade"')

And the generated output is as following:

.. image:: http://gnuplot.sourceforge.net/demo/histograms.1.png
   :width: 350

3.1.3 splot
+++++++++++

.. _surface1.py:

..
    cmd2img:: python3
    :image: surface2.9.png

object-oriented function call:

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    g = gnuplot.Gnuplot(output = '"surface2.9.png"',
            terminal = 'pngcairo enhanced font "arial,10" fontscale 1.0 size 600, 400 ',
            title = '"Interlocking Tori" ',
            dummy = 'u, v',
            key = 'bmargin center horizontal Right noreverse enhanced autotitle nobox',
            style = ['increment default','data lines'],
            parametric = '',
            view = '50, 30, 1, 1',
            isosamples = '50, 20',
            hidden3d = 'back offset 1 trianglepattern 3 undefined 1 altdiagonal bentover',
            xyplane = 'relative 0',
            urange = '[ -3.14159 : 3.14159 ] noreverse nowriteback',
            vrange = '[ -3.14159 : 3.14159 ] noreverse nowriteback')
    g.splot('cos(u)+.5*cos(u)*cos(v),sin(u)+.5*sin(u)*cos(v),.5*sin(v) with lines',
            '1+cos(u)+.5*cos(u)*cos(v),.5*sin(v),sin(u)+.5*sin(u)*cos(v) with lines')

.. _surface2.py:

Direct function call example:

..
    cmd2img:: python3
    :image: surface2.9.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    gnuplot.splot('cos(u)+.5*cos(u)*cos(v),sin(u)+.5*sin(u)*cos(v),.5*sin(v) with lines',
            '1+cos(u)+.5*cos(u)*cos(v),.5*sin(v),sin(u)+.5*sin(u)*cos(v) with lines',
            terminal = 'pngcairo enhanced font "arial,10" fontscale 1.0 size 600, 400 ',
            output = '"surface2.9.png"',
            dummy = 'u, v',
            key = 'bmargin center horizontal Right noreverse enhanced autotitle nobox',
            style = ['increment default','data lines'],
            parametric = '',
            view = '50, 30, 1, 1',
            isosamples = '50, 20',
            hidden3d = 'back offset 1 trianglepattern 3 undefined 1 altdiagonal bentover',
            xyplane = 'relative 0',
            title = '"Interlocking Tori" ',
            urange = '[ -3.14159 : 3.14159 ] noreverse nowriteback',
            vrange = '[ -3.14159 : 3.14159 ] noreverse nowriteback')

And the generated output is as following:

.. image:: http://gnuplot.sourceforge.net/demo/surface2.9.png
   :width: 350

3.1.4 pm3d
++++++++++

iterate.dem

.. _whale1.py:

..
    cmd2img:: python3
    :image: whale.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot

    #http://ayapin-film.sakura.ne.jp/Gnuplot/Pm3d/Part1/whale.html
    g = gnuplot.Gnuplot()
    #g.set(terminal = 'pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 ',
    #        output = '"iterate.2.png"',
    #        noborder = '',
    #        key = ['title "splot for [scan=1:*] \'whale.dat\' index scan" center',
    #              'bmargin center horizontal Right noreverse enhanced autotitle nobox',
    #              'noinvert samplen 0.6 spacing 1 width 0 height 0 ',
    #              'maxcolumns 0 maxrows 6'],
    #        style = 'increment default',
    #        view = '38, 341, 1, 1',
    #        xtics = '',
    #        ytics = '',
    #        ztics = '',
    #        title = '"Iteration over all available data in a file" ',
    #        lmargin = 'at screen 0.09',
    #        rmargin = 'at screen 0.9')
    #g.splot('for [i=1:*] "examples/whale.dat" index i title sprintf("scan %d",i) with lines')

    # Black and white version
    g.splot('"examples/whale.dat" w pm3d',
            term = 'pngcairo size 480,480',
            out = '"whale.png"',
            style = 'line 100 lw 0.1 lc "black"',
            pm3d = 'depth hidden3d ls 100',
            cbrange = '[-0.5:0.5]',
            palette = 'rgb -3,-3,-3',
            colorbox = None,
            border = None,
            key = None,
            zrange = '[-2:2]',
            tics = None,
            view = '60,185,1.5')


.. _whale2.py:

..
    cmd2img:: python3
    :image: whale.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd

    #gnuplot.splot('for [i=1:*] "examples/whale.dat" index i title sprintf("scan %d",i) with lines',
    #        terminal = 'pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 ',
    #        output = '"iterate.2.png"',
    #        border = '',
    #        key = ['title "splot for [scan=1:*] \'whale.dat\' index scan" center',
    #              'bmargin center horizontal Right noreverse enhanced autotitle nobox',
    #              'noinvert samplen 0.6 spacing 1 width 0 height 0 ',
    #              'maxcolumns 0 maxrows 6'],
    #        style = 'increment default',
    #        view = '38, 341, 1, 1',
    #        xtics = '',
    #        ytics = '',
    #        ztics = '',
    #        title = '"Iteration over all available data in a file" ',
    #        lmargin = 'at screen 0.09',
    #        rmargin = 'at screen 0.9')

    # Black and white version
    gnuplot.splot('"examples/whale.dat" w pm3d',
            term = 'pngcairo size 480,480',
            out = '"whale.png"',
            style = 'line 100 lw 0.1 lc "black"',
            pm3d = 'depth hidden3d ls 100',
            cbrange = '[-0.5:0.5]',
            palette = 'rgb -3,-3,-3',
            colorbox = None,
            border = None,
            key = None,
            zrange = '[-2:2]',
            tics = None,
            view = '60,185,1.5')

And the generated output is as following:

.. http://ayapin-film.sakura.ne.jp/Gnuplot/Pm3d/Part1/whale.html
.. image http://gnuplot.sourceforge.net/demo/iterate.2.png
.. image:: http://ayapin-film.sakura.ne.jp/Gnuplot/Pm3d/Part1/whale.png
   :width: 350

3.2 Examples port from matplotlib
---------------------------------

Just for fun, I translate some examples in matplotlib to py-gnuplot:

3.2.1 Stacked bar chart
+++++++++++++++++++++++

..
    .. cmd2img:: python3
        :image: sphx_glr_bar_stacked_001.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    import pandas as pd
    from pygnuplot import gnuplot

    # data is from https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py
    #https://matplotlib.org/_downloads/2ac62a2edbb00a99e8a853b17387ef14/bar_stacked.py
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 35, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    width = 0.35       # the width of the bars: can also be len(x) sequence

    # Plot programme:
    df = pd.DataFrame({'men_means': men_means,
        'women_means': women_means,
        'men_std': men_std,
        'women_std': women_std}, index = labels)
    #print(df)
    gnuplot.plot_data(df,
            'using :($2 + $3):5:xtic(1) with boxerror title "women" lc "dark-orange"',
            'using :2:4 with boxerror title "men" lc "royalblue"',
            style = ['data boxplot', 'fill solid 0.5 border -1'],
            boxwidth = '%s' %(width),
            xrange = '[0.5:5.5]',
            ylabel = '"Scores"',
            title = '"Scores by group and gender"',
            output = '"sphx_glr_bar_stacked_001.png"',
            terminal = 'pngcairo size 640, 480')

Refer to the original script: `Stacked bar chart`_ and the original image:

.. _Stacked bar chart: https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py
.. image:: https://matplotlib.org/_images/sphx_glr_bar_stacked_001.png
   :width: 350

3.2.2 Grouped bar chart with labels
+++++++++++++++++++++++++++++++++++

..
    cmd2img:: python3
            :image: sphx_glr_barchart_001.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    import pandas as pd
    from pygnuplot import gnuplot

    # data is from https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    width = 0.35  # the width of the bars

    # Plot programme:
    df = pd.DataFrame({'men': men_means, 'women': women_means},
            index = labels)
    df.index.name = 'label'
    #print(df)
    gnuplot.plot_data(df,
            'using 2:xticlabels(1) title columnheader(2) lc "web-blue"',
            'using 3:xticlabels(1) title columnheader(3) lc "orange"',
            'using ($0-0.2):($2+1):2 with labels notitle column',
            'using ($0+0.2):($3+1):3 with labels notitle column',
            title = '"Scores by group and gender"',
            xrange = '[-0.5:4.5]',
            yrange = '[0:38]',
            ylabel = '"Scores"',
            style = ['data histogram',
                     'histogram cluster gap 1',
                     'fill solid border -1',
                     'textbox transparent'],
            output = '"sphx_glr_barchart_001.png"',
            terminal = 'pngcairo size 640, 480')

Refer to the original script: `Grouped bar chart with labels`_ and the original image:

.. _Grouped bar chart with labels: https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
.. image:: https://matplotlib.org/_images/sphx_glr_barchart_001.png
   :width: 350

3.2.3 Multiplot Axes Demo
+++++++++++++++++++++++++

..
    cmd2img:: python3
            :image: sphx_glr_axes_demo_001.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd
    import numpy as np

    #https://matplotlib.org/gallery/subplots_axes_and_figures/axes_demo.html#sphx-glr-gallery-subplots-axes-and-figures-axes-demo-py
    #http://gnuplot.sourceforge.net/demo_5.2/bins.html

    # 1) create some data to use for the plot
    np.random.seed(19680801) # Fixing random state for reproducibility
    dt = 0.001
    t = np.arange(0.0, 10.0, dt)
    r = np.exp(-t / 0.05)  # impulse response
    x = np.random.randn(len(t))
    s = np.convolve(x, r)[:len(x)] * dt  # colored noise
    df = pd.DataFrame({'r': r, 'x': x, 's': s}, index = t)
    df.index.name = 't'

    g = gnuplot.Gnuplot(log = True,
            output = '"sphx_glr_axes_demo_001.png"',
            term = 'pngcairo font "arial,10" fontscale 1.0 size 640, 480',
            key = '',
            multiplot = '')

    # 2) Plot the data
    g.plot_data(df.iloc[:1000],
            'using 1:4 with line lw 2 lc "web-blue"',
            title = '"Gaussian colored noise"',
            xlabel = '"time (s)"',
            ylabel = '"current (nA)"',
            xrange = '[0:1]',
            yrange = '[-0.015:0.03]',
            key = None,
            size = ' 1, 1',
            origin = '0, 0')
    g.plot_data(df,
            'using 4 bins=400 with boxes title "20 bins" lw 2 lc "web-blue"',
            title = '"Probability"',
            xlabel = None,
            ylabel = None,
            tics = None,
            xrange = None,
            yrange = None,
            origin = '0.65, 0.56',
            size = '0.24, 0.32',
            object = 'rectangle from graph 0,0 to graph 1,1 behind fc "black" fillstyle solid 1.0')
    g.plot_data(df,
            'using 1:2 with line lw 2 lc "web-blue"',
            title = '"Impulse response"',
            xrange = '[0:0.2]',
            origin = '0.15, 0.56',
            size = '0.24, 0.32')

Refer to the original script: `Multiplot Axes Demo`_ and the original image:

.. _Multiplot Axes Demo: https://matplotlib.org/gallery/subplots_axes_and_figures/axes_demo.html#sphx-glr-gallery-subplots-axes-and-figures-axes-demo-py
.. image:: https://matplotlib.org/_images/sphx_glr_axes_demo_001.png
   :width: 350

3.2.4 control view and zoom 
++++++++++++++++++++++++++++

..
    cmd2img:: python3
            :image: sphx_glr_axes_margins_001.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd
    #https://matplotlib.org/gallery/subplots_axes_and_figures/axes_margins.html#sphx-glr-gallery-subplots-axes-and-figures-axes-margins-py
    g = gnuplot.Gnuplot(log = True,
            output = '"sphx_glr_axes_margins_001.png"',
            term = 'pngcairo font "arial,10" fontscale 1.0 size 640,480',
            multiplot = "")

    g.cmd('f(x) = exp(-x) * cos(2*pi*x)')
    g.plot('sample [x=0:3] "+" using (x):(f(x)) with lines',
            title = '"Zoomed out"',
            key = None,
            xrange = '[-6: 9]',
            yrange = '[-4: 4]',
            xtics = '-5, 5, 5',
            ytics = '-2, 2, 4',
            origin = '0, 0.5',
            size = '0.5, 0.5')
    g.plot('f(x)',
            title = '"Zoomed in"',
            key = None,
            xrange = '[0: 3]',
            yrange = '[-0.2: 0.5]',
            xtics = '0, 1, 2',
            ytics = '-0.2, 0.2, 0.4',
            origin = '0.5, 0.5',
            size = '0.5, 0.5')
    g.plot('f(x)',
            title = None,
            key = None,
            xrange = '[0: 3]',
            yrange = '[-0.7: 1]',
            xtics = '0, 0.5, 3',
            ytics = '-0.5, 0.5, 1',
            origin = '0, 0',
            size = '1, 0.5')


Refer to the original script: `axes_margins.py`_ and the original image:

.. _axes_margins.py: https://matplotlib.org/_downloads/4d3bc54481c3ff3a1ac6712bc2904875/axes_margins.py
.. image:: https://matplotlib.org/_images/sphx_glr_axes_margins_001.png
   :width: 350

3.2.5 Rendering math equation using TeX
+++++++++++++++++++++++++++++++++++++++

We can embed the TeX math equation into the gnuplot generated image by setting
the epslatex terminal, it would be rendered as a .tex file, you can import it
directly or you can convert it to .pdf file and then .png file if needed. this
is the example:

..
    cmd2img:: python3
    :image: pygnuplot_tex_demo.tex

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    from pygnuplot import gnuplot
    import pandas as pd
    # https://matplotlib.org/gallery/text_labels_and_annotations/tex_demo.html#sphx-glr-gallery-text-labels-and-annotations-tex-demo-py
    # http://wap.sciencenet.cn/blog-373392-500657.html
    # https://www.thinbug.com/q/17593917
    g = gnuplot.Gnuplot(log = True,
            output = '"pygnuplot_tex_demo.tex"',
            term = 'epslatex standalone lw 2 color colortext')

    # NOTE: In the following example, we need to escape the "\", that means we
    # should use '\\' or "\\\\" for \
    g.plot('cos(4*pi*x) + 2',
            xlabel = "'\\textbf{time (s)}'",
            ylabel = "'\\textit{Velocity (\N{DEGREE SIGN}/sec)}'",
            title = "'\\TeX\\ is Number $\\displaystyle\\sum_{n=1}^\\infty\\frac{-e^{i\\pi}}{2^n}$!' tc 'red'",
            key = None,
            xrange = '[0: 1]')

I list the script output since it's with the log=True::

    [py-gnuplot 14:56:13] set output "pygnuplot_tex_demo.tex"
    [py-gnuplot 14:56:13] set term epslatex standalone lw 2 color colortext
    [py-gnuplot 14:56:13] set xlabel '\textbf{time (s)}'
    [py-gnuplot 14:56:13] set ylabel '\textit{Velocity (°/sec)}'
    [py-gnuplot 14:56:13] set title '\TeX\ is Number $\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!' tc 'red'
    [py-gnuplot 14:56:13] unset key
    [py-gnuplot 14:56:13] set xrange [0: 1]
    [py-gnuplot 14:56:13] plot cos(4*pi*x) + 2

Refer to the original script: `Rendering math equation using TeX`_ and the original image:

.. _Rendering math equation using TeX: https://matplotlib.org/gallery/text_labels_and_annotations/tex_demo.html#sphx-glr-gallery-text-labels-and-annotations-tex-demo-py
.. image:: https://matplotlib.org/_images/sphx_glr_tex_demo_001.png
   :width: 350

3.2.6 Basic pie chart
+++++++++++++++++++++

..
    cmd2img:: python3
    :image: sphx_glr_pie_features_0011.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf8
    import pandas as pd
    import math
    from pygnuplot import gnuplot

    #http://www.phyast.pitt.edu/~zov1/gnuplot/html/pie.html
    #https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    startangle = math.pi/2

    # Prepare the data: caculate the percentage
    df = pd.DataFrame({'labels': labels, 'sizes': sizes, 'explode': explode})
    df.index.name = 'index'
    df['percentage'] = df['sizes'] / df['sizes'].sum()
    df['end'] = df['percentage'].cumsum()*2*math.pi + startangle
    #df['start'] = df['end'].shift(axis=0, fill_value = 0)
    df['start'] = df['end'].shift(axis=0)
    df = df.fillna(startangle)
    #print(df)

    pie_shade = []
    pie_graph = []

    shade_offset = 0.03
    for k, v in df.iterrows():
        #print(k,v)
        cos = math.cos((v['start']+v['end'])/2)
        sin = math.sin((v['start']+v['end'])/2)

        # If we'd like explode the piece, ad the dx/dy to move the origi point.
        dx = v['explode'] * cos
        dy = v['explode'] * sin

        # make the shade for each piece
        piece = gnuplot.make_plot('cos(t)+%f, sin(t)+%f with filledcurves xy=%f,%f lc "grey80"'
                    %(dx-shade_offset, dy-shade_offset, dx-shade_offset, dy-shade_offset),
                trange = '[%f:%f]' %(v['start'], v['end']),
                xrange = '[-1.5:1.5]',
                yrange = '[-1.5:1.5]')
        pie_shade.append(piece)

        # make the pie and label
        piece = gnuplot.make_plot('cos(t)+%f, sin(t)+%f with filledcurve xy=%f,%f  lt %d'
                    %(dx, dy, dx, dy, k+3),
                trange = '[%f:%f]' %(v['start'], v['end']),
                xrange = '[-1.5:1.5]',
                yrange = '[-1.5:1.5]',
                label = ['1 "%s" at %f, %f center front' %(v['labels'], 1.2*cos+dx, 1.2*sin+dy),
                    '2 "%.1f%%" at %f, %f center front' %(v['percentage']*100, 0.6*cos, 0.6*sin)])
        pie_graph.append(piece)

    gnuplot.multiplot(*pie_shade, *pie_graph,
            output = '"sphx_glr_pie_features_0011.png"',
            terminal = 'pngcairo size 640, 480',
            key = None,
            parametric = '',
            border = '',
            tics = '',
            multiplot = '')

Refer to the original script: `Basic pie chart`_ and the original image:

.. _Basic pie chart: https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
.. image:: https://matplotlib.org/_images/sphx_glr_pie_features_0011.png
   :width: 350

4. Q/A
=======

5. CHANGLOG
=============

1.0 Initial upload;

1.0.3 Now Gnuplot().plot()/splot() supplot set options as parameters.

1.0.7 The pyplot.plot() now can accept both string and pandas.Dataframe as the
first parameter, Further more we need pandas installed at first.

1.0.11 Fix the bug: gnuplot.multiplot() doesn't work.

1.0.15 1) Add an example of comparing the object-oriented interface call and
global class-less function call in multiplot() in multiplot() in
multiplot() in multiplot(). 2) remove some duplicate setting line.

1.0.19 Add a log options to enable the log when run the script.

1.1 Upgrade to 1.1: 1) Submodule pyplot is depreciated. 2) To plot python generated
data we use gnuplot.plot_data() and gnuplot.splot_data().


1.1.2 Enhancement: If it's multiplot mode, automatically call the following
Gnuplot to unset the label:

    g.unset('for [i=1:200] label i')

1.1.3 Enhancement: When plotting the python generated data, we set the
seperator to "," for easy using it in csv file.
1.1.5 Bug fix: on some case it exit exceptionally.
1.1.8 Remove some Chinese comments to remove the "UnicodeDecodeError" for some users.

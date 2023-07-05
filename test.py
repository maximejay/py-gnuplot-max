#pip3 install --no-compile .
from pygnuplot import gnuplot
import numpy as np
import pandas as pd
data={"x":np.zeros(10)+1.,"y":np.arange(0,10)}
data2={"x":np.zeros(10)+1.,"y":np.arange(0,10)*2.}
df1=pd.DataFrame(data)
df2=pd.DataFrame(data2)

g=gnuplot.Gnuplot(log=True)
g.plot_data(df1,'using 1:3 w l')


g.load_dataframe(df1,'df1')
g.load_dataframe(df2,'df2')


# ~ g.plot_dataframe('$df1 using 1:3 w l')
# ~ g.plot_dataframe('$df2 using 1:3 w l')
# ~ g.plot_dataframe_finalise()


g.plot_cmd('$df1 using 1:3 w l')
g.plot_cmd('$df2 using 1:3 w l')
g.plot_cmd('$df2 using 1:2 w l')
g.plot_finalise()

g.close()

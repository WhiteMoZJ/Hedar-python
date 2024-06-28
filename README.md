# Hedar Testset Python
This test set originates from the [Hedar test set](http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm), rewritten in Python.

## Usage
To use the test set, simply put the whole folder `hedar_testset_python` in your project folder. For example, to use the `XXX` function, you can do the following:
```python
from hedar_testset_python import XXX
XXX.get_result('''input parameters''')
```
or
```python
import hedar_testset_python
hedar_testset.XXX.get_result('''input parameters''')
```
where `XXX` is the name of the function you want to use.
or just import the whole module at once
```python
from hedar_testset_python import *
XXX.get_result('''input parameters''')
```
While some functions using the `numpy` library, so you need to install it first. You can install it using the following command:
```bash
pip install numpy
```


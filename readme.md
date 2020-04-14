### OPF - Ordered Pairing Functions 
#### _for Python 3.7+ with support for arbitrarily large integers_ 

Sub-second algorithm for pairing and unpairing non-negative integers up to 7MB long in my laptop.

Please contribute with more pairing and benhcmarks, maybe we find an underlying bottleneck we could fix! :)

#### Usage

```python
import cantor

assert (23, 45) == cantor.unpair(cantor.pair(23, 45))

import elegant

assert (23, 45) == elegant.unpair(elegant.pair(23, 45))
```

Check `test.py` for more examples of usage. This package will be made available over `pypi` once some more pairing algos are added. If you want to publish it, please be kind to let me know before hand. :)

#### References
* https://en.wikipedia.org/wiki/Pairing_function
* https://drhagen.com/blog/superior-pairing-function/

------
**PS.:** Python 3.8 includes `math.isqrt`, supposedly slower than the `gmpy2` library, dependency for this project. For higher portability just upgrade python and change the libraries to remove this dependency. Kudos to [Anders Kaseorg and Mathmandan](https://stackoverflow.com/questions/15390807/integer-square-root-in-python) for pointing this out this fantastic library.

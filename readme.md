### OPF - Ordered Pairing Functions 
##### _for Python 3.7+ with support for arbitrarily large integers_ 

Sub-second algorithm for pairing and unpairing non-negative integers. Tests execute under one second with integers up to 7MB large in my laptop. Numbers larger than that take more, even minutes.

Please contribute with more pairing and benhcmarks, maybe we find an underlying bottleneck we could fix! :)

### Usage
Example with numbers much larger than C `ULONG_MAX` for 64bit that is `18446744073709551615`.

```python
import time
import cantor
import elegant

if __name__ == '__main__':
    # cantor
    start = time.time()
    assert (87917298379182739871892379817239871982379817239871928371923791827398172397129387192379182379182379182739182739187239817329871923791827981723,
            981729837981273971298379812739817239871923791827398172398712983767468675465746172649162486347649289817239) == \
           cantor.unpair(cantor.pair(87917298379182739871892379817239871982379817239871928371923791827398172397129387192379182379182379182739182739187239817329871923791827981723,
                                     981729837981273971298379812739817239871923791827398172398712983767468675465746172649162486347649289817239))
    end = time.time()
    print('cantor\t', '{0:.10f} secs'.format(end - start))
    # elegant
    start = time.time()
    assert (87917298379182739871892379817239871982379817239871928371923791827398172397129387192379182379182379182739182739187239817329871923791827981723,
            981729837981273971298379812739817239871923791827398172398712983767468675465746172649162486347649289817239) == \
           elegant.unpair(elegant.pair(87917298379182739871892379817239871982379817239871928371923791827398172397129387192379182379182379182739182739187239817329871923791827981723,
                                       981729837981273971298379812739817239871923791827398172398712983767468675465746172649162486347649289817239))
    end = time.time()
    print('elegant\t', '{0:.10f} secs'.format(end - start))

# Results:
# cantor	 0.0001599789 secs
# elegant	 0.0000128746 secs
```

Check `test.py` for more examples of usage. This package will be made available over `pypi` once some more pairing algos are added. If you want to publish it, please be kind to let me know before hand. :)

### References
* [Wikipedia](https://en.wikipedia.org/wiki/Pairing_function)
* [Matthew Szudzik's Elegant Pairing](http://szudzik.com/ElegantPairing.pdf)

#### To be implemented
* [Efficient PFs, and why you should care](https://www.researchgate.net/publication/220181086_Efficient_Pairing_Functions_-_and_Why_You_Should_Care)
* [Dr. Hagen's Superior PF](https://drhagen.com/blog/superior-pairing-function/)

------
**PS.:** Python 3.8 includes `math.isqrt`, supposedly slower than the `gmpy2` library, dependency for this project. For higher portability just upgrade python and change the libraries to remove this dependency. Kudos to [Anders Kaseorg and Mathmandan](https://stackoverflow.com/questions/15390807/integer-square-root-in-python) for pointing this out this fantastic library.

# Bayeslite

[![Build Status](https://travis-ci.org/probcomp/bayeslite.svg?branch=master)](https://travis-ci.org/probcomp/bayeslite)
[![Anaconda-Server Version Badge](https://anaconda.org/probcomp/bayeslite/badges/version.svg)](https://anaconda.org/probcomp/bayeslite)
[![Anaconda-Server Installer Badge](https://anaconda.org/probcomp/bayeslite/badges/installer/conda.svg)](https://conda.anaconda.org/probcomp)
[![Anaconda-Server Platform Badge](https://anaconda.org/probcomp/bayeslite/badges/platforms.svg)](https://anaconda.org/probcomp/bayeslite)

BQL interpretation and storage for BayesDB.
Please see http://probcomp.csail.mit.edu/software/bayesdb for more information.

## Installing

The easiest way to install bayeslite is to use the
[package](https://anaconda.org/probcomp/bayeslite) on Anaconda Cloud.
Please follow [these instructions](https://github.com/probcomp/iventure/blob/master/docs/conda.md).

## Expectations

Users and contributors should expect **rapidly and dramatically
shifting code and behavior** at this time.

**THIS SOFTWARE SHOULD NOT BE EXPECTED TO TREAT YOUR DATA SECURELY.**

## Contributing

Our compatibility aim is to work on probcomp machines and members'
laptops, and to provide scripts and instructions that make it not too
hard to re-create our environments elsewhere. Pulls for polished
packaging, broad installability, etc. are not appropriate
contributions at this time.

Please run local tests before sending a pull request:

```
$ ./check.sh
```

That does not run the complete test suite, only the smoke tests, but
is usually good enough. For the full suite:

```
$ ./check.sh tests shell/tests
```

## Documentation

To build the documentation, which is also available
[online](http://probcomp.csail.mit.edu/dev/bayesdb/doc/),
install [sphinx](http://www.sphinx-doc.org/en/master/)
and then run the following command:

```
$ make doc
```

The result will be placed in `build/doc`, with one subdirectory per
output format.

To build only one output format, e.g. HTML because you don't want to
install TeX:

```
$ make html
```

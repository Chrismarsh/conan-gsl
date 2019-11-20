conan-gsl
=========

Conan package for the C/C++ `GNU Scientific Library (GSL)`_.

Requires CMake, sources are fetched from `ampl's GitHub repository`_.


.. warning::
    This is a Work In Progress, has only been lightly tested. Feel free to
    fork / submit PR / report issues
    (https://bitbucket.org/tkhyn/conan-gsl/issues/new)

Cloned from: https://bitbucket.org/tkhyn/conan-gsl/src/default/


How to use
----------

While this recipe is not field-tested and is not available on conan-center_,
you may follow these steps to install the GNU Scientific Library as a conan
dependency:

1. Download ``conanfile.py`` from this repository into an empty folder (cloning
   this repository also works)
2. Run ``conan create . temp/libs`` from that folder. This is where issues may
   arise (please report them along with your OS and compiler)
3. Add ``GSL/2.4@temp/libs`` to your ``conanfile.txt``


.. _`GNU Scientific Library (GSL)`: http://www.gnu.org/software/gsl/
.. _`ampl's GitHub repository`: https://github.com/ampl/gsl
.. _conan-center: https://bintray.com/conan/conan-center

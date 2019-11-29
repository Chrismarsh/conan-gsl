from conans import ConanFile, CMake, tools


class GslConan(ConanFile):
    """
    Conan recipe for the GNU Scientific Library
    http://www.gnu.org/software/gsl/
    """

    name = "gsl"
    version = "2.4"
    license = "GNU GPL"
    url = "http://www.gnu.org/software/gsl/"
    description = "GNU Scientific Library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        # downloading the archive is faster than cloning the repository
        # we're using ampl's github repo as it contains CMakeLists.txt already
        tools.download('https://github.com/ampl/gsl/archive/v2.4.0.tar.gz',
                       'gsl-2.4.0.tar.gz')
        tools.unzip('gsl-2.4.0.tar.gz')

    def build(self):
        cmake = CMake(self)
        if(self.options.shared):
            cmake.definitions["BUILD_SHARED_LIBS"]=True

        cmake.configure(source_folder="gsl-2.4.0")
        cmake.build()

    def package(self):
        # all include files should go in include/gsl
        self.copy("*.h", dst="include/gsl", src="gsl")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("libgsl*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gsl"]

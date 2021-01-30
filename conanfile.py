from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class GslConan(ConanFile):
    """
    Conan recipe for the GNU Scientific Library
    http://www.gnu.org/software/gsl/
    """

    name = "gsl"
    license = "GNU GPL"
    url = "http://www.gnu.org/software/gsl/"
    description = "GNU Scientific Library"
    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False]
    }
    default_options = {
        "shared": True
    }
    generators = "cmake"

    _source_subfolder = 'gsl'

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("gsl-{}".format(self.version), self._source_subfolder)
        tools.replace_in_file(self._source_subfolder+"/configure", r"-install_name \$rpath/", "-install_name @rpath/")


    def build(self):
        autotools = AutoToolsBuildEnvironment(self)

        configure_args = [ ]

        if(self.options.shared):
            configure_args.append("--enable-shared")
        if(not self.options.shared):
            configure_args.append("--enable-static")

        #disable warnings for travis ci
        if os.getenv("CI") is not None:
            # print("Detected CI, disabling GSL warnings")
            val = os.environ.get("CFLAGS", "")
            os.environ["CFLAGS"] = val + " -w"

            val = os.environ.get("CPPFLAGS", "")
            os.environ["CPPFLAGS"] = val + " -w"

        with tools.chdir(self._source_subfolder):

            autotools.configure(args=configure_args)
            autotools.make()
            autotools.install()


    def package(self):
        # all include files should go in include/gsl
        self.copy("*.h", dst="include/gsl", src="gsl")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("libgsl*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gsl","gslcblas"]

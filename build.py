from cpt.packager import ConanMultiPackager
from collections import defaultdict

if __name__ == "__main__":
    builder = ConanMultiPackager(cppstds=[14],
                                archs=["x86_64"],
                                build_types=["Release"])
                        
    builder.add_common_builds(pure_c=False, shared_option_name=False)
    builder.remove_build_if(lambda build: build.settings["compiler.libcxx"] == "libstdc++") # old ABI


    builder.run()

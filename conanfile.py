from conans import ConanFile, CMake, tools
import os


class Area51Conan(ConanFile):
    name = "area51"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/simmplecoder/area51"
    settings = "os", "compiler", "build_type", "arch"
    options = {"BuildTests": [True, False]}
    default_options = "BuildTests=True"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/simmplecoder/area51.git")
        self.run("cd area51")

    def package(self):
#        print(os.getcwd())
#        path = os.getcwd()
#        build_folder = "../package/" + path.split('/')[-1]
        self.copy("*.hpp", dst="include", src= "area51/src")
        self.copy("*.cpp", dst="test_src", src= "area51/tests", keep_path=True)
        #self.copy("*", dst="test_exec", src= "build/test_exec", keep_path=True)
#        self.copy("*.so", dst="lib", keep_path=False)
#        self.copy("*.dylib", dst="lib", keep_path=False)
#        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]

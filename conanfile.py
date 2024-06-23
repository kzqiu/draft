from conan import ConanFile
# from conan.tools.cmake import cmake_layout


class DraftRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("asio/1.30.2")

    # def layout(self):
    #     cmake_layout(self)

    def build_requirements(self):
        self.tool_requires("cmake/3.22.6")

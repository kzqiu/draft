# draft: modal tui editor

## Requirements

- python
- CMake

## Build Instructions

### Conan

```bash
# virtual environment and installs
$ python -m venv .venv/
$ source .venv/bin/activate
$ pip install -r requirements.txt

# install project dependencies
$ conan profile detect --force
$ conan install . --output-folder=build --build=missing
```

### CMake

```bash
$ cd build

# Release
$ cmake --preset conan-release
$ cmake --build --preset conan-release

# Debug
$ cmake --preset conan-debug
$ cmake --build --preset conan-debug
```

# Python, C++ ... Let's talk!

## Project setup

### Prerequisite

1. Python versions and virtual environments are controlled with (the very convenient) [pyenv](https://github.com/pyenv/pyenv). Pyenv installation depends on the OS used:
> - MacOS: 
>    `brew update`
>    `brew install pyenv`
> - Windows:
>    follow [pyenv-win](https://github.com/pyenv-win/pyenv-win)

2. Additionaly, a docker implementation is also provided to generalize setup for everyone. ([Get started](https://github.com/pyenv-win/pyenv-win) with Docker if you haven't already.)


## A) Running using Docker

An ubuntu docker image with all the required dependencies is provided by `docker/Dockerfile`. The C++ binding is built in `docker/build_binding.sh` and both the C++ executable and the DLL in python are called by `docker/entrypoint.sh`. The entire project setup can be executed by:
> 
>   `docker compose build binding`  
>   `docker compose up binding`
>

## B) Running Local

1. **Configure project setup**

A virtual environment with all required packages is created by the simple command:

- MacOS: `make setup`
- Windows: `make setup-win` (make sure to use a bash-like shell or follow similar commands)

2. **Build the C++ binding**

Building the binding executable & the DLL does depend on your setup and installed compiler.  
This is an example using [VS Code build Tasks](https://code.visualstudio.com/docs/cpp/config-linux) on MacOS with an installed GCC compiler, but other build configurations will work as well. 

<details>
  <summary>Example `.vscode/tasks.json` (click to expand)</summary>
  
  ```
{
	"version": "2.0.0",
    "tasks": [
		{
			"type": "cppbuild",
			"label": "Build with GCC 11.2.0",
			"command": "/usr/local/bin/g++-11",
			"args": [
				"-std=c++20",
				"-o",
				"${workspaceFolder}/binding_cpp_root/build/bin/binding",
				"-I",
				"${workspaceFolder}/binding_cpp_root/include/binding",
				"${workspaceFolder}/binding_cpp_root/src/*.cpp"
			],
			"options": {
				"cwd": "${workspaceFolder}"
			},
			"problemMatcher": [
				"$gcc"
			],
			"group": "build",
			"detail": "compiler: /usr/local/bin/g++-11"
		},
		{
			"type": "cppbuild",
			"label": "Create Library with GCC (Shared Object)",
			"command": "/usr/local/bin/g++-11",
			"args": [
				"-std=c++20",
				"-o",
				"${workspaceFolder}/binding_cpp_root/build/lib/binding.so",
				"-fpic",
				"-shared",
				"-I",
				"${workspaceFolder}/binding_cpp_root/include/binding",
				"${workspaceFolder}/binding_cpp_root/src/*.cpp"
			],
			"options": {
				"cwd": "${workspaceFolder}"
			},
			"problemMatcher": [
				"$gcc"
			],
			"group": {
				"kind": "build",
				"isDefault": true
			},
			"detail": "compiler: /usr/local/bin/g++-11"
		},
	]
}
  ```
</details>

3. **Run & Test the binding**

When compiled correctly. The executable can be started as demonstrated in:
- MacOS: `make executable`
- Windows: `make executable-win`  

And you should be able to run the python binding with:
- MacOS: `make main`
- Windows: `make main-win`

Note that there are also two unittests provided. The first one is testing the operation of the cpp binding given known input and output. The second one verifies the similarity between Python and C++ implementations. All unit tests, with a resulting code coverage report, can be executed using:
- MacOS: `make tests`
- Windows: `make tests-win`

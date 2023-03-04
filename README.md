# BioText
Generate unique handwrited text. Good for abstracts, essay, summary, precis, conspectus



# Build from source

### Windows + Visual Studio

1. Download <a href=https://cmake.org/download/>CMake</a>.
2. Download source code from this repository.
3. Unzip source code.
4. Open command line (win + R >> cmd) and type "cmake-gui".
5. In the 'Where is the source code' field type YOUR_PATH_TO_SOURCE_CODE_FOLDER/bio-text.
6. Where to build the binaries type the same text, but add the folder for the binaries.
7. Click 'Configure' and specify your IDE, wait for it and click 'Configure' again, 'Generate' next.
8. Select the 'Release' as build target instead of 'Debug'.
9. As done, copy 'default.frag' and 'default.vert' files from 'res' where your executable file and run executable.

### Ubuntu + Code::Blocks

- Install Code::Blocks and CMake GUI app:
```
sudo apt update
sudo apt install codeblocks cmake-gui
```

- BioText must have these packages also:
```
sudo apt install gcc-8 g++-8
```

- Download source code and unzip it.

- Open CMake:
```
cmake-gui
```
- In the 'Where is the source code' field type YOUR_PATH_TO_SOURCE_CODE_DIR/bio-text.
- Where to build the binaries type the same text, but add the directory for the binaries.
- Click 'Configure' and select 'CodeBlocks - Unix Makefiles', wait for it and click 'Configure' again, 'Generate' next.
- Run biotext.cbp, which was generated.
- Select the 'biotext' as build target instead of 'all' then build the target.
- As done, copy 'default.frag' and 'default.vert' files from 'res' where your executable file and run executable.

cmake_minimum_required(VERSION 3.8)

set(PROJECT_NAME biotext)
project(${PROJECT_NAME} VERSION 1.0.0)
set(CMAKE_CXX_STANDARD 17)

if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
	set(CMAKE_CXX_COMPILER /usr/bin/g++-8)
endif()

add_subdirectory(src)

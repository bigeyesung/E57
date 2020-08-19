cmake_minimum_required(VERSION 3.5)
project(hello_library)


############################################################
# Create an executable
############################################################


find_library(LIB_TO_INCLUDE libhello_library.a ${CMAKE_SOURCE_DIR}/lib )
include_directories(${CMAKE_SOURCE_DIR}/include)
SET( APP_EXE MyExecutable )
add_executable(${APP_EXE} src/main2.cpp)
target_link_libraries(${APP_EXE} ${LIB_TO_INCLUDE})


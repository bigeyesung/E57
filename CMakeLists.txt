cmake_minimum_required ( VERSION 3.0)



project( myProject )

set( SOURCE_FILES ${CMAKE_SOURCE_DIR}/src/main.cpp )
message( ${CMAKE_SOURCE_DIR}/src/main.cpp )
message( "${CMAKE_SOURCE_DIRs}/src/main.cpp" )
add_library( MyStaticLib STATIC IMPORTED )
set_property( TARGET MyStaticLib PROPERTY IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/lib/libMyStaticLib.a )
add_executable( myProject ${SOURCE_FILES} )
target_include_directories(myProject PRIVATE ${CMAKE_SOURCE_DIR}/include )
target_link_libraries( myProject ${CMAKE_SOURCE_DIR}/lib/libMyStaticLib.a )

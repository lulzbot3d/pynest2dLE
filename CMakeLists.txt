cmake_policy(SET CMP0091 NEW)
project(pynest2dle)
cmake_minimum_required(VERSION 3.20)

find_package(nest2dle REQUIRED)
find_package(cpython REQUIRED)

find_package(standardprojectsettings REQUIRED)
find_package(sipbuildtool REQUIRED)

add_library(pynest2d INTERFACE)
use_threads(pynest2d)

target_link_libraries(pynest2d INTERFACE nest2dle::nest2dle cpython::cpython)
add_sip_module(pynest2d)
install_sip_module(pynest2d)


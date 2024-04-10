# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "Back-app_autogen"
  "CMakeFiles\\Back-app_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\Back-app_autogen.dir\\ParseCache.txt"
  )
endif()

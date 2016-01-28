#!/usr/bin/env python

import sys, subprocess, os, glob

full_path = os.path.realpath(__file__)
base_dir = os.path.dirname(full_path)
src_dir = os.path.join(base_dir, "project", "src")
bin_dir = os.path.join(base_dir, "project", "bin")
lib_dir = os.path.join(base_dir, "project", "lib")
tools_dir = os.path.join(base_dir, "tools")

junit_jar_path = os.path.join(tools_dir, "junit-4.12.jar")
hamcrest_jar_path = os.path.join(tools_dir, "hamcrest-core-1.3.jar")
cp_jar_path = os.path.join(tools_dir, "cp-1.2.6.jar")

src_files = glob.glob(src_dir + "/*.java")
lib_jar_files = glob.glob(lib_dir + "/*.jar")

lib_arg = ":".join(lib_jar_files) + ":" + lib_dir

# compile
compile_args = ["javac", "-cp", lib_arg + ":" + junit_jar_path, "-d", bin_dir]
compile_args.extend(src_files)
compile_res = subprocess.call(compile_args)

if compile_res != 0 : 
    print ("compile failed! (javac exited with " + str(compile_res) + ")");
    exit(compile_res)

# run
classpath_arg = junit_jar_path + ":" + cp_jar_path + ":" + hamcrest_jar_path + ":" + tools_dir + ":" + bin_dir + ":" + lib_arg

run_res = subprocess.call(["java", "-cp", classpath_arg, "RunAllSuite"])

if run_res != 0 : 
    print ("run failed! (java exited with "+ str(run_res) + ")")
    exit(compile_res)


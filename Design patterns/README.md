# Project Architectural design patterns

## Required

* PySide6

## Overview

Aim of this project is to create a simple application that will be interconnector between „old” and „new” application in enterprise using few of patterns presented during lecture.

## Application functionality description

Application will take input file in format specify later in this document and convert it to one of the outputs specify later.

To perform this this task there will be simple user interface that will allow user to:
* Open file dialog box
* Save file dialog box
* Output format selection

Output format will be:
* Semicolon separated csv
* XML file

Each design pattern used in code need to be described by comments in program code that will clearly state what and where was used.

## Input format description

This will be text file (csv or txt extension) where each column will be TAB separated.

Date Time Speed Distance Description
* Date will be provided in YYYY/DD/MM format
* Time will be in 12-hr format hh:mm:ss AM/PM
* Speed will be in m/s
* Distance will be provided km
* Description will be alphanumeric characters

## Output formats
### CSV

Date Time Speed Distance Description

* Date should be DD.MM.YYYY format
* Time should be HH:mm:ss 24hr
* Speed will be in knots (nautical miles per hour)
* Distance will be provided Nautical miles
* Description will be alphanumeric characters

# Resulting .exe located in ./dist/testconv.exe
#!/usr/bin/env python
# -*- coding: utf8 -*-
import os, sys, re
file = open("sub-03_ses-test_task-linebisection_events.tsv", "r+").read()
Correct_Task = []
Incorrect_Task = []
Response_Control = []
No_Response_Control = []
No_Response_Task = []
pCorrect_Task = re.compile(r"(\d.+)\s1\s1.0\sCorrect_Task$",re.MULTILINE)
pIncorrect_Task = re.compile(r"(\d.+)\s1\s1.0\sIncorrect_Task$",re.MULTILINE)
pResponse_Control = re.compile(r"(\d.+)\s1\s1.0\sResponse_Control$",re.MULTILINE)
pNo_Response_Control = re.compile(r"(\d.+)\s1\s1.0\sNo_Response_Control$",re.MULTILINE)
pNo_Response_Task = re.compile(r"(\d.+)\s1\s1.0\sNo_Response_Task$",re.MULTILINE)
matchesCorrect_Task = pCorrect_Task.finditer(file)
matchesIncorrect_Task = pIncorrect_Task.finditer(file)
matchesResponse_Control = pResponse_Control.finditer(file)
matchesNo_Response_Control = pNo_Response_Control.finditer(file)
matchesNo_Response_Task = pNo_Response_Task.finditer(file)
for CT in matchesCorrect_Task:
	Correct_TaskTiming = CT.groups()
	print Correct_TaskTiming
	Correct_Task += [Correct_TaskTiming[0]]
	fileCorrect_Task = open("Correct_Task.txt","w+")
	fileCorrect_Task.write(' '.join(Correct_Task))
for IncT in matchesIncorrect_Task:
	Incorrect_TaskTiming = IncT.groups()
	print Incorrect_TaskTiming
	Incorrect_Task += [Incorrect_TaskTiming[0]]
	fileIncorrect_Task = open("Incorrect_Task.txt","w+")
	fileIncorrect_Task.write(' '.join(Incorrect_Task))
for RC in matchesResponse_Control:
	Response_ControlTiming = RC.groups()
	print Response_ControlTiming
	Response_Control += [Response_ControlTiming[0]]
	fileResponse_Control = open("Response_Control.txt","w+")
	fileResponse_Control.write(' '.join(Response_Control))
for NRC in matchesNo_Response_Control:
	No_Response_ControlTiming = NRC.groups()
	print No_Response_ControlTiming
	No_Response_Control += [No_Response_ControlTiming[0]]
	fileNo_Response_Control = open("No_Response_Control.txt","w+")
	fileNo_Response_Control.write(' '.join(No_Response_Control))
for NRT in matchesNo_Response_Task:
	No_Response_TaskTiming = NRT.groups()
	print No_Response_TaskTiming
	No_Response_Task += [No_Response_TaskTiming[0]]
	fileNo_Response_Task = open("Response_Control.txt","w+")
	fileNo_Response_Task.write(' '.join(No_Response_Task))	

# This system (file/program) is the thing protecting this PC from PC System-shutdowns that may have to reset this PC. WARNING: DO NOT DELETE/END-TASK THIS PROCESS!

import auto

if task.killed("Isass"):
  print("You are about to be logged off.","Please save your work and log off immediadly. The system process has ran into an error and we have reported it to AEGiS Headquarters®. Your PC will shutdown in 1 minute.")
  nop(60)
  taskKill("SYSTEM_PROCESS")
  set("RSoD",true)
  
if task.killed("AEG@Defender"):
  print("You are about to be logged off.","Please save your work and restart immediadly. The AEGiS Desktop Defender has suddenly crashed. Please restart your computer. Your PC will auto-restart 1 minute later.")
  nop(60)
  taskKill("SYSTEM_PROCESS")
  set("RSoD",true)
  
if task.killed("SYSTEM_PROCESS"):
  set("RSoD",true)
  
if task.killed("AEGiS_Contacter"):
  print("0.emote you don't have permission to crash this process.".format(EMOTE10))

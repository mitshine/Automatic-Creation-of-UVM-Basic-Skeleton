import os

os.system("python create_top_module.py")
os.system("python create_test.py")
os.system("python create_interface.py")
os.system("python create_packet.py")
os.system("python create_sequence.py")
os.system("python create_sequencer.py")
os.system("python create_environment.py")
os.system("python create_agent.py")
os.system("python create_driver.py")
os.system("python create_monitor.py")
os.system("python create_scoreboard.py")
os.system("python create_design_under_test.py")

print("UVM Skeleton Created Successfully")
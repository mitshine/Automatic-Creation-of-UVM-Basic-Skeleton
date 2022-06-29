f = open("./uvm_codes/sequencer.sv", "w")

f.write('`include "uvm_macros.svh"\n')
f.write('import uvm_pkg::*;\n')
f.write('`include "packet.sv"\n')
f.write('\n')
f.write('class sequencer extends uvm_sequencer #(packet);\n')
f.write('\n')
f.write('   `uvm_component_utils(sequencer)\n')
f.write('\n')
f.write('   function new(input string name, uvm_component parent=null);\n')
f.write('      super.new(name, parent);\n')
f.write('   endfunction : new\n')
f.write('\n')
f.write('endclass : sequencer\n')

f.close()

#open and read the file after the appending:
f = open("./uvm_codes/sequencer.sv", "r")
print(f.read())
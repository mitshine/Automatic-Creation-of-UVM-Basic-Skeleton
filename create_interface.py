f = open("./uvm_codes/intf.sv", "w")

f.write('interface intf(input bit clk);\n')
f.write('   // declare all the input and output signals as logic.\n   // for example: logic [19:0] a; logic [19:0]   q;\n')
f.write('\n')
f.write('   clocking pck @(posedge clk);\n')
f.write('      output a;  // include input as output for modport declaration for making it bi-directional signals\n')
f.write('      input q;  // include output as input for modport declaration for making it bi-directional signals\n')
f.write('   endclocking: pck\n')
f.write('\n')
f.write('endinterface: ifc\n')

f.close()

#open and read the file after the appending:
f = open("./uvm_codes/intf.sv", "r")
print(f.read())
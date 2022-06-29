f = open("./uvm_codes/subscriber.sv", "w")

f.write('class func_cov extends uvm_subscriber #(seq_item);\n')
f.write('  covergroup cg;\n')
f.write('  ...\n')
f.write('  endgroup\n')
f.write('\n')
f.write('  function void write (seq_item req);\n')
f.write('    ...\n')
f.write('    cg.sample();\n')
f.write('  endfunction\n')
f.write('endclass\n')
f.write('\n')
f.write('// Env class connects broadcaster and subscriber class using analysis port connection.\n')
f.write('class env extends uvm_env;\n')
f.write('  `uvm_component_utils(env)\n')
f.write('  agent agt;\n')
f.write('  func_cov fc;\n')
f.write('\n')
f.write('  function new(string name = "env", uvm_component parent = null);\n')
f.write('    super.new(name, parent);\n')
f.write('  endfunction\n')
f.write('\n')
f.write('  function void build_phase(uvm_phase phase);\n')
f.write('    super.build_phase(phase);\n')
f.write('    agt = agent::type_id::create("agt", this);\n')
f.write('    fc = func_cov::type_id::create("fc", this);\n')
f.write('  endfunction\n')
f.write('\n')
f.write('  function void connect_phase(uvm_phase phase);\n')
f.write('    agt.mon.item_collect_port.connect(fc.analysis_export); // Here, Monitor behaves as a broadcaster.\n')
f.write('  endfunction\n')
f.write('endclass\n')

f.close()

#open and read the file after the appending:
f = open("./uvm_codes/subscriber.sv", "r")
print(f.read())
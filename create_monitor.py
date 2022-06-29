f = open("./uvm_codes/monitor.sv", "w")

f.write('`include "uvm_macros.svh"\n')
f.write('import uvm_pkg::*;\n')
f.write('`include "intf.sv"\n')
f.write('`include "packet.sv"\n')
f.write('\n')
f.write('class monitor extends uvm_monitor;\n')
f.write('\n')
f.write('     `uvm_component_utils(monitor)\n')
f.write('\n')
f.write('     virtual intf vif;\n')
f.write('     uvm_analysis_port#(packet) ap;\n')
f.write('\n')
f.write('     function new(string name, uvm_component parent);\n')
f.write('         super.new(name, parent);\n')
f.write('         ap = new("ap", this);\n')
f.write('     endfunction\n')
f.write('\n')
f.write('     function void build();\n')
f.write('         uvm_report_info(get_full_name(),"Build", UVM_LOW);\n')
f.write('         if (!uvm_config_db#(virtual intf)::get(this, "", "vif", vif)) begin\n')
f.write('            `uvm_fatal("AXI/MON/NOVIF", "No virtual interface specified for this monitor instance")\n')
f.write('         end\n')
f.write('     endfunction\n')
f.write('\n')
f.write('     function void connect();\n')
f.write('         uvm_report_info(get_full_name(),"Connect", UVM_LOW);\n')
f.write('     endfunction\n')
f.write('\n')
f.write('     function void end_of_elaboration();\n')
f.write('         uvm_report_info(get_full_name(),"End_of_elaboration", UVM_LOW);\n')
f.write('     endfunction\n')
f.write('\n')
f.write('     function void start_of_simulation();\n')
f.write('         uvm_report_info(get_full_name(),"Start_of_simulation", UVM_LOW);\n')
f.write('     endfunction\n')
f.write('\n')
f.write('     task run_phase(uvm_phase phase);\n')
f.write('         uvm_report_info(get_full_name(),"Run", UVM_LOW);\n')
f.write('         super.run_phase(phase);\n')
f.write('         forever@(posedge vif.clk) begin\n')
f.write('            packet tr;\n')
f.write('            tr = packet::type_id::create("tr", this);\n')
f.write('            // drive virtual interface signals to packet in monitor to send the packet to scoreboard.\n')
f.write('            tr.a = vif.a;\n')
f.write('            tr.q = vif.q;\n')
f.write('            // access and call an in-built write function in scoreboard through analysis port.\n')
f.write('            // monitor will write all the packet values or virtual interface signal values via analysis port to scoreboards write function.\n')
f.write('            ap.write(tr);\n')
f.write('         end\n')
f.write('     endtask\n')
f.write('\n')
f.write('     function void extract();\n')
f.write('         uvm_report_info(get_full_name(),"Extract", UVM_LOW);\n')
f.write('     endfunction\n')
f.write('\n')
f.write('     function void check();\n')
f.write('         uvm_report_info(get_full_name(),"Check", UVM_LOW);\n')
f.write('     endfunction\n')
f.write('\n')
f.write('     function void report();\n')
f.write('         uvm_report_info(get_full_name(),"Report", UVM_LOW);\n')
f.write('     endfunction\n')
f.write('\n')
f.write('endclass\n')

f.close()

#open and read the file after the appending:
f = open("./uvm_codes/monitor.sv", "r")
print(f.read())
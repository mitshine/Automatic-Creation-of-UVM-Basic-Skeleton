f = open("./uvm_codes/driver.sv", "w")

f.write('`include "uvm_macros.svh"\n')
f.write('import uvm_pkg::*;\n')
f.write('`include "intf.sv"\n')
f.write('`include "packet.sv"\n')
f.write('\n')
f.write('class driver extends uvm_driver #(packet);\n')
f.write('     `uvm_component_utils(driver)\n')
f.write('\n')
f.write('     virtual intf vif;\n')
f.write('\n')
f.write('     function new(string name, uvm_component parent);\n')
f.write('         super.new(name, parent);\n')
f.write('     endfunction\n')
f.write('\n')
f.write('     function void build();\n')
f.write('         uvm_report_info(get_full_name(),"Build", UVM_LOW);\n')
f.write('         if (!uvm_config_db#(virtual intf)::get(this, "", "vif", vif)) begin\n')
f.write('            `uvm_fatal("AXI/DRV/NOVIF", "No virtual interface specified for this driver instance")\n')
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
f.write('\n')
f.write('         // initialize all the virtual interface signals to "0".\n')
f.write('         vif.a    <=  0;\n')
f.write('         vif.q    <=  0;\n')
f.write('\n')
f.write('         forever begin\n')
f.write('            packet tr;\n')
f.write('            @ (vif.clk);\n')
f.write('            seq_item_port.get_next_item(tr);\n')
f.write('            write(tr);\n')
f.write('            seq_item_port.item_done();\n')
f.write('          end\n')
f.write('     endtask\n')
f.write('\n')
f.write('     virtual protected task write(packet tr);\n')
f.write('        if(tr.rst == 0) begin\n')
f.write('            // connect and drive the packet signals to virtual interface signals, write packet signals to virtual interface\n')
f.write('            vif.a   <= tr.a;\n')
f.write('            vif.q    <= tr.q;\n')
f.write('        end\n')
f.write('        else begin\n')
f.write('            // drive virtual interface signals with random values.\n')
f.write('            @(posedge vif.clk)\n')
f.write('            vif.a = $random();\n')
f.write('            vif.q = 1;\n')
f.write('        end\n')
f.write('     endtask: write\n')
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
f = open("./uvm_codes/driver.sv", "r")
print(f.read())
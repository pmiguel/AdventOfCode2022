#!/bin/env ruby

def read_file(file_name)
    file = File.open(file_name)
    data = file.readlines.map(&:chomp)    
    file.close

    return data
end

data = read_file "in1.txt"

current_elf = 0
current_top = current_elf

elf_data = Hash.new
elf_data[current_elf] = {elf_total: 0, elf_list: []}

data.each do |line| 
    if line.empty?
        if elf_data[current_elf][:elf_total] > elf_data[current_top][:elf_total]
            current_top = current_elf
        end
        current_elf += 1
        elf_data[current_elf] = {elf_total: 0, elf_list: []}
    else
        parsed = line.to_i
        elf_data[current_elf][:elf_total] += parsed
        elf_data[current_elf][:elf_list] = elf_data[current_elf][:elf_list].append(parsed)
    end
end

puts elf_data[current_top][:elf_total]

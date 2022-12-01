#!/bin/env ruby

file = File.open("in1.txt")
data = file.readlines.map(&:chomp)    
file.close

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

# Part1
puts "Top1 Most #{elf_data[current_top][:elf_total]}"

top_3_total = elf_data
    .map { |k,v| v[:elf_total] }
    .sort()
    .reverse()
    .slice(0, 3)
    .sum()

puts "Top3 Total: #{top_3_total}"

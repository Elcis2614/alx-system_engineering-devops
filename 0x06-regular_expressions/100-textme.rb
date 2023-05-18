#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+*[0-9a-z]*)\] \[to:(\+*\d+)\] \[flags:(.*\d)\]/i).join(",")

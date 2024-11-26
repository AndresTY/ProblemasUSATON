10.times do |i|
  File.open("secret/#{i+1}.ans", mode: "w") do |f|
      f.write `python solution.py < secret/#{i+1}.in`
  end
end

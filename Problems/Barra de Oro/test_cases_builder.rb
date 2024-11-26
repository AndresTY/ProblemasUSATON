10.times do |i|
  File.open("secret/#{i+1}.in", mode: "w") do |f|
    10.times do |j|
      f.write "#{rand(1..20000)}\n"
    end
    f.write 0
  end
end

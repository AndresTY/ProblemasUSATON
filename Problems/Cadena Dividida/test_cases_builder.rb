def string_to_build(t)
  value = ""
  string_size = rand(2..500)
  string_size.times do
    value += rand(0..1).to_s
  end
  value
end

10.times do |i|
  File.open("secret/#{i+1}.in", mode: "w") do |f|
    t_value = rand(1..200)
    f.write "#{t_value}\n"
    t_value.times do |t|
      f.write "#{string_to_build(t)}\n"
    end
  end
end

def format_x(beginning: false)
  if beginning
    inf_value = 1
  else
    inf_value = 0
  end

  rand(inf_value..99).to_s
end

def format_y
  y = rand(0..99)
  return "0#{y}" if y < 9
  y.to_s
end

10.times do |i|
  File.open("secret/#{i+1}.in", mode: "w") do |f|
    n_days = rand(1..100)
    f.write "#{n_days}\n"

    f.write "$#{format_x(beginning: true)}.#{format_y}\n"
    (n_days).times do |n|
      f.write "$#{format_x}.#{format_y}\n"
    end
  end
end

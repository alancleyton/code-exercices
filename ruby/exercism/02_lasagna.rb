=begin
  Lasagna

  https://exercism.org/tracks/ruby/exercises/lasagna
=end

class Lasagna
  EXPECTED_MINUTES_IN_OVEN = 40
  LAYER_MULTIPLIER = 2

  def remaining_minutes_in_oven(actual_minutes_in_oven)
    Lasagna::EXPECTED_MINUTES_IN_OVEN - actual_minutes_in_oven
  end

  def preparation_time_in_minutes(layers)
    layers * Lasagna::LAYER_MULTIPLIER
  end

  def total_time_in_minutes(number_of_layers:, actual_minutes_in_oven:)
    preparation_time_in_minutes(number_of_layers) + actual_minutes_in_oven
  end
end

lasagna = Lasagna.new
puts lasagna.remaining_minutes_in_oven(30)
puts lasagna.preparation_time_in_minutes(2)
puts lasagna.total_time_in_minutes(number_of_layers: 3, actual_minutes_in_oven: 20)
